import pytest
import pandas as pd
from analysis import (
    calculate_average_heart_rate,
    count_stress_labels,
    average_session_duration
)

def sample_df():
    """Helper DataFrame for testing."""
    return pd.DataFrame({
        "timestamp": ["2025-01-01", "2025-01-02"],
        "heart_rate": [70, 90],
        "stress_label": ["low", "high"],
        "session_duration": [25, 40]
    })

# ------------------- PASSING TEST CASES -------------------

def test_average_heart_rate():
    df = sample_df()
    assert calculate_average_heart_rate(df) == 80


def test_stress_count():
    df = sample_df()
    result = count_stress_labels(df)
    assert result["low"] == 1
    assert result["high"] == 1


def test_avg_session_duration():
    df = sample_df()
    assert average_session_duration(df) == 32.5


def test_empty_dataframe():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        calculate_average_heart_rate(empty_df)


# ------------------- INTENTIONALLY FAILING TEST CASES -------------------

def test_wrong_average_heart_rate():
    """Fail on purpose: expected wrong average."""
    df = pd.DataFrame({
        "timestamp": ["2025-01-01", "2025-01-02"],
        "heart_rate": [60, 90],
        "stress_label": ["low", "high"],
        "session_duration": [30, 40]
    })
    # Actual average = 75, test expects 80
    assert calculate_average_heart_rate(df) == 80


def test_missing_stress_label_key():
    """Fail on purpose: key does not exist."""
    df = pd.DataFrame({
        "timestamp": ["2025-01-01"],
        "heart_rate": [70],
        "stress_label": ["low"],
        "session_duration": [30]
    })
    counts = count_stress_labels(df)
    # KeyError expected because "high" does not exist
    assert counts["high"] == 1


def test_empty_df_wrong_error():
    """Fail on purpose: expecting wrong exception type."""
    df = pd.DataFrame()
    # Function raises ValueError, but we expect TypeError
    with pytest.raises(TypeError):
        calculate_average_heart_rate(df)
