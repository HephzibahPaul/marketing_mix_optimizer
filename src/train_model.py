import pandas as pd
import pickle
import numpy as np
import os
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def main():
    print("📂 Loading dataset...")
    df = pd.read_csv("data/marketing_data.csv")

    # Log transforms for diminishing returns (add 1 to avoid log(0))
    df["tv_log"] = np.log1p(df["tv"])
    df["radio_log"] = np.log1p(df["radio"])
    df["social_log"] = np.log1p(df["social"])
    df["search_log"] = np.log1p(df["search"])
    df["price_log"] = np.log1p(df["price"])
    df["competitor_log"] = np.log1p(df["competitor_spend"])

    feature_cols = [
        "tv_log",
        "radio_log",
        "social_log",
        "search_log",
        "price_log",
        "competitor_log",
    ]

    X = df[feature_cols]
    y = df["sales"]

    print("🤖 Training stable MMM model (Ridge + scaling)...")

    # Pipeline: scale features + Ridge regression for stability
    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("ridge", Ridge(alpha=1.0, random_state=42)),
        ]
    )

    model.fit(X, y)

    model_path = os.path.join("src", "model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print("✅ Stable MMM model trained and saved to", model_path)


if __name__ == "__main__":
    main()
