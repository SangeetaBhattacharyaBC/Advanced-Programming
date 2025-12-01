import pytest
import pandas as pd
from data_ingestion import load_data
import os

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data("non_existing.csv")


def test_missing_columns(tmp_path):
    # Create a file missing required columns
    file = tmp_path / "bad.csv"
    pd.DataFrame({"timestamp": [1], "heart_rate": [80]}).to_csv(file, index=False)

    with pytest.raises(KeyError):
        load_data(file)


def test_negative_heart_rate(tmp_path):
    file = tmp_path / "neg.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01"],
        "heart_rate": [-50],
        "stress_label": ["high"],
        "session_duration": [30]
    }).to_csv(file, index=False)

    with pytest.raises(ValueError):
        load_data(file)


def test_valid_data(tmp_path):
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
