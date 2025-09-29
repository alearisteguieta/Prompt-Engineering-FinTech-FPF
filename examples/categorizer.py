import pandas as pd
import numpy as np
import time
import pickle
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from typing import List, Dict, Any

# --- Configuration and Mock Data Setup ---
# Define the set of categories for financial categorization
CATEGORIES = [
    "Groceries", "Dining", "Utilities", "Rent", "Salary",
    "Transport", "Entertainment", "Health", "Investment", "Misc"
]

# Mock function to simulate a pre-trained model loading process
def generate_mock_model():
    """Generates a simple mock ML pipeline for demonstration."""
    print("Generating mock model for Expense Categorization...")
    
    # 1. Mock Training Data
    data = {
        'description': [
            "Trader Joe's", "Starbucks Coffee", "Electricity Bill", "Monthly Rent Payment",
            "Uber Ride", "Netflix Subscription", "Hospital Visit Co-pay", "Monthly Dividend",
            "Whole Foods Market", "Local Diner Lunch", "Water & Sewage", "Bus Pass",
            "Movie Tickets", "Gym Membership", "Deposit - Paycheck"
        ],
        'category': [
            "Groceries", "Dining", "Utilities", "Rent",
            "Transport", "Entertainment", "Health", "Investment",
            "Groceries", "Dining", "Utilities", "Transport",
            "Entertainment", "Health", "Salary"
        ]
    }
    df = pd.DataFrame(data)
    
    # 2. Define the Model Pipeline (Vectorizer + Classifier)
    # Using Logistic Regression for its speed, meeting the < 500ms requirement.
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', max_features=1000)),
        ('clf', LogisticRegression(random_state=42, n_jobs=-1))
    ])
    
    # 3. Train the model
    pipeline.fit(df['description'], df['category'])
    
    # 4. Save the mock model
    joblib.dump(pipeline, 'mock_expense_model.joblib')
    print("Mock model saved as 'mock_expense_model.joblib'")
    return pipeline

# Attempt to load or generate the mock model upon script execution
try:
    ML_MODEL = joblib.load('mock_expense_model.joblib')
    print("Pre-trained mock model loaded.")
except FileNotFoundError:
    ML_MODEL = generate_mock_model()
    
# --- Expense Categorization Engine Class ---

class ExpenseCategorizationEngine:
    """
    ML Service for categorizing financial transactions.
    
    Designed for low-latency inference (Target: < 500ms per transaction)
    as required by the Financial Prompt Framework (FPF).
    """

    def __init__(self, model: Pipeline):
        """Initializes the engine with the pre-loaded ML model."""
        self.model = model
        self.categories = CATEGORIES
        
    def preprocess_data(self, transaction: Dict[str, Any]) -> str:
        """
        Preprocesses a single transaction record for model inference.
        In a real system, this would normalize text, handle missing data, etc.
        """
        # Ensure 'description' is a string and handle potential NaNs or None
        description = str(transaction.get('description', '')).lower().strip()
        
        # Simple cleaning: remove common financial noise
        description = description.replace('purchase at', '').replace('online payment', '')
        return description

    def categorize_transaction(self, transaction: Dict[str, Any]) -> Dict[str, Any]:
        """
        Performs the expense categorization inference.
        
        :param transaction: A dictionary representing a single transaction.
        :return: The transaction dictionary with the 'predicted_category' field added.
        """
        start_time = time.perf_counter()
        
        # 1. Preprocessing
        processed_text = self.preprocess_data(transaction)
        
        if not processed_text:
            transaction['predicted_category'] = "Uncategorized/Error"
            print("Warning: Empty transaction description. Categorization skipped.")
            return transaction

        # 2. Inference
        try:
            # Predict the category using the loaded pipeline (vectorizer + classifier)
            prediction = self.model.predict([processed_text])[0]
            
            # 3. Confidence/Probability Score (Optional but recommended in FinTech ML)
            probabilities = self.model.predict_proba([processed_text])[0]
            confidence_score = np.max(probabilities)
            
            # 4. Apply result
            transaction['predicted_category'] = prediction
            transaction['confidence_score'] = float(f"{confidence_score:.4f}")
            
        except Exception as e:
            # Robust error handling for FinTech systems
            print(f"Error during categorization for transaction {transaction.get('id', 'N/A')}: {e}")
            transaction['predicted_category'] = "System Error"
            transaction['confidence_score'] = 0.0

        end_time = time.perf_counter()
        latency_ms = (end_time - start_time) * 1000
        transaction['latency_ms'] = float(f"{latency_ms:.3f}")

        if latency_ms > 500:
            print(f"ALERT: Categorization latency exceeded 500ms target: {latency_ms:.3f}ms")
            
        return transaction

# --- Demonstration and Testing Block ---
if __name__ == "__main__":
    
    engine = ExpenseCategorizationEngine(model=ML_MODEL)
    print("\n--- Expense Categorization Engine Demo ---")

    # Mock Input Transactions (Real-world transaction data structure)
    test_transactions = [
        {"id": "t_001", "amount": -55.99, "date": "2025-09-29", "description": "Payment to Electric Co"},
        {"id": "t_002", "amount": 1500.00, "date": "2025-09-29", "description": "Deposit - September Salary"},
        {"id": "t_003", "amount": -12.50, "date": "2025-09-30", "description": "Lunch at Pizzeria"},
        {"id": "t_004", "amount": -450.00, "date": "2025-10-01", "description": "Roth IRA Contribution"},
        {"id": "t_005", "amount": -89.45, "date": "2025-10-02", "description": "Groceries at Safeway"},
        {"id": "t_006", "amount": -9.99, "date": "2025-10-03", "description": "Hulu Streaming Service"}
    ]

    print(f"\nProcessing {len(test_transactions)} transactions...")
    
    processed_results = []
    
    for tx in test_transactions:
        result = engine.categorize_transaction(tx)
        processed_results.append(result)
        
    print("\n--- Categorization Results ---")
    for result in processed_results:
        print(f"ID: {result['id']} | Desc: '{result['description']:<30}' | Predicted Category: {result['predicted_category']:<15} | Confidence: {result['confidence_score']:.2f} | Latency: {result['latency_ms']:.3f}ms")
        
    # Validation of Performance Metric (FPF Requirement)
    avg_latency = np.mean([r['latency_ms'] for r in processed_results])
    
    print(f"\n--- FPF Performance Metric Validation ---")
    print(f"Total transactions processed: {len(processed_results)}")
    print(f"Average latency per transaction: {avg_latency:.3f}ms")
    
    if avg_latency < 500:
        print("SUCCESS: Average latency meets the target (< 500ms).")
    else:
        print("FAILURE: Average latency exceeds the target (>= 500ms).")

    # Clean up the mock model file
    import os
    if os.path.exists('mock_expense_model.joblib'):
        os.remove('mock_expense_model.joblib')
        print("\nCleaned up 'mock_expense_model.joblib'.")
