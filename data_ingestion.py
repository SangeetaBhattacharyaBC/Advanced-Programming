import pandas as pd
import os

def load_data(filepath):
    """
    Load CSV data with proper error handling.
    Returns a pandas DataFrame.
    """

    # File missing
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise ValueError(f"Failed to read CSV file: {e}")

    # Required columns
    required = ['timestamp', 'heart_rate', 'stress_label', 'session_duration']
    missing_cols = [col for col in required if col not in df.columns]

    if missing_cols:
        raise KeyError(f"Missing required columns: {missing_cols}")

    # Remove rows with missing values
    df = df[required].dropna()

    # Check invalid values
    if (df['heart_rate'] < 0).any():
        raise ValueError("Invalid heart rate: heart_rate cannot be negative")

    if (df['session_duration'] < 0).any():
        raise ValueError("Invalid duration: session_duration cannot be negative")

    return df
