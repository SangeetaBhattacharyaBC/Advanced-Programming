import pandas as pd
import os

def load_data(filepath):
    """
    Load CSV data with robust error handling.
    Returns a cleaned pandas DataFrame.
    """

    # --- 1. Check if file exists ---
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # --- 2. Try reading CSV file ---
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise ValueError(f"Failed to read CSV file: {e}")

    # --- 3. Ensure required columns exist ---
    required = ['timestamp', 'heart_rate', 'stress_label', 'session_duration']
    missing_cols = [col for col in required if col not in df.columns]

    if missing_cols:
        raise KeyError(f"Missing required columns: {missing_cols}")

    # --- 4. Drop rows with missing values ---
    df = df[required].dropna()

    # --- 5. Validate numerical data ---
    if (df['heart_rate'] < 0).any():
        raise ValueError("Invalid heart rate: heart_rate cannot be negative")

    if (df['session_duration'] < 0).any():
        raise ValueError("Invalid duration: session_duration cannot be negative")

    return df
