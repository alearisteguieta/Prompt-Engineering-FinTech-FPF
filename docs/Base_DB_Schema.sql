-- Base_DB_Schema.sql
-- Deliverable from Layer 1: Strategic Architecture Prompt
-- Purpose: Defines the core data structure to support Account Aggregation (Mint)
-- and Automated Investment Advisory (Betterment) logic.
-- Database: PostgreSQL is recommended for UUIDs and JSONB support.
-- Encrypted fields present in the full version of the documents supplied in the repository" (encrypted_first_name, encrypted_last_name, encrypted_metadata) 

--------------------------------------------------------------------------------
-- 1. USERS Table (Client Profiles)
-- Key entities: User identity, authentication hash, and financial profile (risk).
-- Security Requirement: Passwords must be hashed using Bcrypt.
--------------------------------------------------------------------------------
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL, -- Stores Bcrypt hash
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    risk_profile VARCHAR(50) NOT NULL CHECK (risk_profile IN ('Conservative', 'Moderate', 'Aggressive')),
    mfa_enabled BOOLEAN DEFAULT FALSE -- Supports MFA security requirement (Layer 3)
);

COMMENT ON TABLE users IS 'User profiles, including hashed password and financial risk assessment.';


--------------------------------------------------------------------------------
-- 2. FINANCIAL_ACCOUNTS Table
-- Stores linked bank accounts data and Plaid tokens.
-- Security Requirement: Plaid access tokens must be encrypted (AES-256).
--------------------------------------------------------------------------------
CREATE TABLE financial_accounts (
    account_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    account_name VARCHAR(100) NOT NULL,
    institution_name VARCHAR(100),
    account_type VARCHAR(50), -- e.g., 'checking', 'savings', 'investment'
    -- The Plaid access token must be encrypted at rest (AES-256).
    plaid_access_token TEXT NOT NULL,
    current_balance NUMERIC(15, 2),
    is_active BOOLEAN DEFAULT TRUE
);

COMMENT ON COLUMN financial_accounts.plaid_access_token IS 'Plaid access token must be stored as AES-256 Ciphertext (PCI DSS compliant).';


--------------------------------------------------------------------------------
-- 3. TRANSACTIONS Table
-- Stores all individual financial transactions for budget and ML categorization.
--------------------------------------------------------------------------------
CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    account_id UUID NOT NULL REFERENCES financial_accounts(account_id) ON DELETE RESTRICT,
    transaction_date DATE NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    description TEXT,
    -- ML Categorization Engine output (supports Layer 2 logic)
    ml_category VARCHAR(100),
    is_pending BOOLEAN DEFAULT FALSE,
    date_imported TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_transactions_user_date ON transactions (user_id, transaction_date DESC);


--------------------------------------------------------------------------------
-- 4. PORTFOLIO_HOLDINGS Table
-- Stores the current investment holdings for MPT/Tax-Loss Harvesting engine inputs.
--------------------------------------------------------------------------------
CREATE TABLE portfolio_holdings (
    holding_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    account_id UUID REFERENCES financial_accounts(account_id) ON DELETE SET NULL, -- Links to an investment account
    asset_symbol VARCHAR(20) NOT NULL, -- e.g., 'VOO', 'BND', 'AAPL'
    quantity NUMERIC(15, 5) NOT NULL,
    cost_basis NUMERIC(15, 2), -- Required for Tax-Loss Harvesting calculations
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


--------------------------------------------------------------------------------
-- 5. PORTFOLIO_RECOMMENDATIONS Table
-- Stores the historical output of the MPT and Tax-Loss Harvesting algorithms (Layer 2).
--------------------------------------------------------------------------------
CREATE TABLE portfolio_recommendations (
    recommendation_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    run_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    strategy_used VARCHAR(50) NOT NULL CHECK (strategy_used IN ('MPT_Sharpe', 'MPT_Volatility', 'Tax_Loss_Harvesting')),
    -- Optimal weights in JSON format (JSONB for PostgreSQL is efficient)
    optimal_allocation JSONB NOT NULL,
    expected_return_annual NUMERIC(8, 4),
    expected_volatility NUMERIC(8, 4)
);

CREATE INDEX idx_recommendations_user_date ON portfolio_recommendations (user_id, run_date DESC);
