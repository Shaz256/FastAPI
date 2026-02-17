"""
Preprocessing utilities for ML pipeline
Author: Shaziya Sayed
"""

import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(path: str) -> pd.DataFrame:
    """Load dataset"""
    return pd.read_csv(path)


def basic_checks(df: pd.DataFrame) -> None:
    """Print quick diagnostics"""
    print("Shape:", df.shape)
    print("\nMissing values:\n", df.isna().sum())
    print("\nClass distribution:\n", df["purchased"].value_counts())


def split_data(df: pd.DataFrame):
    """Train-test split"""

    X = df.drop(columns=["customer_id", "purchased"])
    y = df["purchased"]

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
