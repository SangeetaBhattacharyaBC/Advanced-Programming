import pytest
import pandas as pd
from analysis import (
    calculate_average_heart_rate,
    count_stress_labels,
    average_session_duration
)

def sample_df():
    return pd.DataFrame({
        "timestamp": ["2025-01-01", "2025-01-02"],
        "heart_rate": [70, 90],
        "stress_label": ["low", "high"],
        "session_duration": [25, 40]
    })


def test_average_heart_rate():
    df = sample_df()
    assert calculate_average_heart_rate(df) == 80


def test_negative_heart_rate():
    df = sample_df()
    df.loc[1, "heart_rate"] = -10
    with pytest.raises(ValueError):
        calculate_average_heart_rate(df)


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
