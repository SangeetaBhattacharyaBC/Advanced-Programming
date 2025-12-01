import pandas as pd

def calculate_average_heart_rate(df):
    """Calculate average heart rate with error handling."""
    if df.empty:
        raise ValueError("Dataset is empty")

    if (df['heart_rate'] < 0).any():
        raise ValueError("Negative heart rate detected")

    return df['heart_rate'].mean()


def count_stress_labels(df):
    """Count occurrences of each stress label."""
    if df.empty:
        raise ValueError("Dataset is empty")

    return df['stress_label'].value_counts().to_dict()


def average_session_duration(df):
    """Calculate average session duration."""
    if df.empty:
        raise ValueError("Dataset is empty")

    if (df['session_duration'] < 0).any():
        raise ValueError("Negative session duration detected")

    return df['session_duration'].mean()
