import os
import time
from typing import Any, Dict, List
import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
--- Configuration and Mock Data Setup ---
CATEGORIES: List[str] = [
"Groceries", "Dining", "Utilities", "Rent", "Salary",
"Transport", "Entertainment", "Health", "Investment", "Misc"
]
MODEL_PATH = "mock_expense_model.joblib"
def generate_mock_model() -> Pipeline:
"""
Generates and persists a simple mock TF-IDF + Logistic Regression pipeline for demo purposes.
Keeps the example fast and deterministic for portfolio latency checks.
"""
print("Generating mock model for Expense Categorization...")
data = {
"description": [
"Trader Joe's", "Starbucks Coffee", "Electricity Bill", "Monthly Rent Payment",
"Uber Ride", "Netflix Subscription", "Hospital Visit Co-pay", "Monthly Dividend",
"Whole Foods Market", "Local Diner Lunch", "Water & Sewage", "Bus Pass",
"Movie Tickets", "Gym Membership", "Deposit - Paycheck"
],
"category": [
"Groceries", "Dining", "Utilities", "Rent",
"Transport", "Entertainment", "Health", "Investment",
"Groceries", "Dining", "Utilities", "Transport",
"Entertainment", "Health", "Salary"
]
}
df = pd.DataFrame(data)
pipeline: Pipeline = Pipeline(
steps=[
("tfidf", TfidfVectorizer(stop_words="english", max_features=1000)),
liblinear supports predict_proba and n_jobs
("clf", LogisticRegression(solver="liblinear", random_state=42, n_jobs=-1))
]
)
pipeline.fit(df["description"], df["category"])
joblib.dump(pipeline, MODEL_PATH)
print(f"Mock model saved as '{MODEL_PATH}'")
return pipeline
def load_or_create_model() -> Pipeline:
try:
model = joblib.load(MODEL_PATH)
print("Pre-trained mock model loaded.")
return model
except FileNotFoundError:
return generate_mock_model()
class ExpenseCategorizationEngine:
"""
ML service for categorizing financial transactions.
Designed for low-latency inference (Target: < 500 ms p95) as defined in the docs.
"""
def init(self, model: Pipeline):
self.model = model
self.categories = CATEGORIES
@staticmethod
def preprocess_data(transaction: Dict[str, Any]) -> str:
"""
Minimal text normalization to keep the example simple and fast.
"""
description = str(transaction.get("description", "")).lower().strip()
return description.replace("purchase at", "").replace("online payment", "")
def categorize_transaction(self, transaction: Dict[str, Any]) -> Dict[str, Any]:
"""
Returns the transaction with predicted_category, confidence_score, latency_ms.
"""
start = time.perf_counter()
processed = self.preprocess_data(transaction)
if not processed:
transaction["predicted_category"] = "Uncategorized"
transaction["confidence_score"] = 0.0
transaction["latency_ms"] = 0.0
return transaction
try:
pred = self.model.predict([processed])[0]
proba = self.model.predict_proba([processed])[0]
confidence = float(np.max(proba))
transaction["predicted_category"] = str(pred)
transaction["confidence_score"] = round(confidence, 4)
except Exception as e:
transaction["predicted_category"] = "System Error"
transaction["confidence_score"] = 0.0
print(f"Categorization error (id={transaction.get('id','N/A')}): {e}")
latency_ms = (time.perf_counter() - start) * 1000.0
transaction["latency_ms"] = round(float(latency_ms), 3)
if latency_ms > 500:
print(f"ALERT: latency {latency_ms:.3f} ms > 500 ms target")
return transaction
if name == "main":
model = load_or_create_model()
engine = ExpenseCategorizationEngine(model=model)
print("n--- Expense Categorization Engine Demo ---")
test_transactions: List[Dict[str, Any]] = [
{"id": "t_001", "amount": -55.99, "date": "2025-09-29", "description": "Payment to Electric Co"},
{"id": "t_002", "amount": 1500.00, "date": "2025-09-29", "description": "Deposit - September Salary"},
{"id": "t_003", "amount": -12.50, "date": "2025-09-30", "description": "Lunch at Pizzeria"},
{"id": "t_004", "amount": -450.00, "date": "2025-10-01", "description": "Roth IRA Contribution"},
{"id": "t_005", "amount": -89.45, "date": "2025-10-02", "description": "Groceries at Safeway"},
{"id": "t_006", "amount": -9.99, "date": "2025-10-03", "description": "Hulu Streaming Service"},
]
results: List[Dict[str, Any]] = [engine.categorize_transaction(tx) for tx in test_transactions]
print("n--- Categorization Results ---")
for r in results:
print(
f"ID: {r['id']} | Desc: '{r['description']:<28}' | "
f"Pred: {r['predicted_category']:<14} | Conf: {r['confidence_score']:.2f} | "
f"Latency: {r['latency_ms']:.3f} ms"
)
avg_latency = float(np.mean([r["latency_ms"] for r in results]))
print("n--- Portfolio Metric Check ---")
print(f"Average latency per transaction: {avg_latency:.3f} ms")
print("OK: < 500 ms target" if avg_latency < 500 else "WARN: >= 500 ms target")
Optional cleanup for demo
if os.path.exists(MODEL_PATH):
os.remove(MODEL_PATH)
print(f"nCleaned up '{MODEL_PATH}'.")
