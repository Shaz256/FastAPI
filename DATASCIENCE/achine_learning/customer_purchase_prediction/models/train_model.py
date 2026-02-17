"""
Customer Purchase Prediction Model
Author: Shaziya Sayed
Purpose: End-to-end ML workflow
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from utils.preprocess import load_data, split_data, basic_checks


DATA_PATH = "../data/customer_data.csv"


def train():

    print("=== Loading Data ===")
    df = load_data(DATA_PATH)

    basic_checks(df)

    print("\n=== Splitting Data ===")
    X_train, X_test, y_train, y_test = split_data(df)

    print("\n=== Training Model ===")
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    print("\n=== Evaluating ===")
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    print("Accuracy:", round(accuracy_score(y_test, preds), 4))
    print("ROC AUC:", round(roc_auc_score(y_test, probs), 4))
    print("\nClassification Report:\n")
    print(classification_report(y_test, preds))

    return model


if __name__ == "__main__":
    train()
