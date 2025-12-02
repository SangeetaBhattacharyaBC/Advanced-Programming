# Brings in pytest for testing, pandas to create CSV files, load_data() function being tested

import pytest
import pandas as pd
from data_ingestion import load_data

# ------------------- PASSING TEST CASES -------------------

def test_valid_data(tmp_path): 
# A temporary CSV file is created, A DataFrame with correct columns is written to it, load_data() loads the file
# The test checks: The row count, The heart-rate value
# This confirms the function works under normal conditions.
    
    """Check that valid CSV loads correctly."""
    file = tmp_path / "good.csv"
    df_in = pd.DataFrame({
        "timestamp": ["2025-01-01"],
        "heart_rate": [75],
        "stress_label": ["normal"],
        "session_duration": [40]
    })
    df_in.to_csv(file, index=False)

    df = load_data(file)
    assert len(df) == 1
    assert df['heart_rate'].iloc[0] == 75


def test_missing_file():
# Trying to load a file that doesn’t exist
# Test passes only if load_data raises FileNotFoundError
    
    """Expect FileNotFoundError for missing file."""
    with pytest.raises(FileNotFoundError):
        load_data("non_existing.csv")


def test_missing_columns(tmp_path):
# CSV file missing required columns (e.g., no stress label, no session duration)
# Test expects a KeyError
# Ensures the ingestion function validates required columns
    
    """Expect KeyError if required columns are missing."""
    file = tmp_path / "bad.csv"
    pd.DataFrame({"timestamp": [1], "heart_rate": [80]}).to_csv(file, index=False)
    with pytest.raises(KeyError):
        load_data(file)


def test_negative_heart_rate(tmp_path):
# A valid CSV is created but heart_rate = -50
# Function should reject negative values
# Test expects a ValueError
    
    """Expect ValueError for negative heart rate."""
    file = tmp_path / "neg.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01"],
        "heart_rate": [-50],
        "stress_label": ["high"],
        "session_duration": [30]
    }).to_csv(file, index=False)
    with pytest.raises(ValueError):
        load_data(file)


# ------------------- INTENTIONALLY FAILING TEST CASES -------------------

def test_wrong_heart_rate_value(tmp_path):
# CSV contains heart_rate = 75
# Test checks if the value equals 100, which is incorrect
# This test will fail every time, by design.
    
    """Fail on purpose: expected wrong heart rate."""
    file = tmp_path / "good2.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01"],
        "heart_rate": [75],
        "stress_label": ["normal"],
        "session_duration": [40]
    }).to_csv(file, index=False)

    df = load_data(file)
    # Fail: 75 != 100
    assert df['heart_rate'].iloc[0] == 100


def test_wrong_error_type(tmp_path):
# Negative heart rate → real function raises ValueError
# Test incorrectly expects KeyError
# This test also fails on purpose.
    
    """Fail on purpose: expecting wrong exception type."""
    file = tmp_path / "neg2.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01"],
        "heart_rate": [-10],
        "stress_label": ["high"],
        "session_duration": [20]
    }).to_csv(file, index=False)

    # Actually raises ValueError, but we check for KeyError
    with pytest.raises(KeyError):
        load_data(file)
