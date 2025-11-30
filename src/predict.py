import os
import pickle
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict_sales(tv, radio, social, search, price, competitor):
    """
    Predict sales using the non-linear MMM model.
    Includes:
    - log transforms (same as training)
    - clipping to avoid negative sales
    """

    # Basic safety: prevent negative spends
    tv = max(tv, 0)
    radio = max(radio, 0)
    social = max(social, 0)
    search = max(search, 0)
    price = max(price, 1)          # avoid log(0) and ₹0 price
    competitor = max(competitor, 0)

    tv_log = np.log1p(tv)
    radio_log = np.log1p(radio)
    social_log = np.log1p(social)
    search_log = np.log1p(search)
    price_log = np.log1p(price)
    competitor_log = np.log1p(competitor)

    X = np.array(
        [[tv_log, radio_log, social_log, search_log, price_log, competitor_log]]
    )

    prediction = model.predict(X)[0]

    # Hard business rule: sales cannot be negative
    prediction = max(prediction, 0)

    # Optional: you could cap extremely huge predictions if needed
    return round(float(prediction), 2)
