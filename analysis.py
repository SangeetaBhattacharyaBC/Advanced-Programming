import pandas as pd

def calculate_average_heart_rate(df):
    """Calculate average heart rate with error handling."""
    if df.empty:
        raise ValueError("Dataset is empty") /*An empty dataset means we cannot compute averages.*/

    if (df['heart_rate'] < 0).any():
        raise ValueError("Negative heart rate detected") /*Heart rate cannot be negative → protects data integrity.*/

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
        raise ValueError("Negative session duration detected") /*Session duration can’t be negative → ensures logical correctness.*/

    return df['session_duration'].mean()
