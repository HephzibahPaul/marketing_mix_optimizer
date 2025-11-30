# src/optimizer.py

import numpy as np


def optimize_budget(total_budget: float, price: float, competitor_spend: float) -> dict:
    """
    Simple ROI-based budget optimizer.

    Inputs:
        total_budget      - total marketing budget (₹)
        price             - product price per unit (₹)
        competitor_spend  - estimated competitor spend (₹)

    Output dict has:
        tv, radio, social, search, total_spend, predicted_sales, roi
    """

    # --- 1. Base effectiveness assumptions per channel ---
    # Higher = more responsive to spend
    # (You can tweak these to match your story in interviews)
    base_effectiveness = np.array([
        0.90,   # TV
        0.55,   # Radio
        1.10,   # Social
        1.00    # Search
    ])

    # --- 2. Competition factor ---
    # If competitors spend a lot relative to your budget,
    # overall effectiveness slightly drops.
    if total_budget <= 0:
        total_budget = 1.0

    competition_ratio = competitor_spend / (total_budget + 1e-6)
    # Clamp impact between 0.7 and 1.0
    competition_factor = float(np.clip(1.0 - 0.15 * competition_ratio, 0.7, 1.0))

    # --- 3. Convert effectiveness to budget weights ---
    weights = base_effectiveness / base_effectiveness.sum()
    channel_spend = weights * total_budget  # TV, Radio, Social, Search

    # --- 4. Diminishing returns model for units sold ---
    # units = Σ alpha_c * log(1 + spend_c)
    alpha = np.array([
        0.030,   # TV
        0.016,   # Radio
        0.040,   # Social
        0.035    # Search
    ]) * competition_factor

    log_terms = np.log1p(channel_spend)
    predicted_units = float((alpha * log_terms).sum() * 1000)  # scaled for realism

    predicted_sales = predicted_units * price

    # --- 5. ROI calculation ---
    roi = 0.0
    if total_budget > 0:
        roi = (predicted_sales - total_budget) / total_budget * 100

    # Round values for presentation
    tv, radio, social, search = [round(x, 2) for x in channel_spend]
    predicted_sales = round(predicted_sales, 2)
    roi = round(roi, 1)
    total_spend = round(total_budget, 2)

    return {
        "tv": tv,
        "radio": radio,
        "social": social,
        "search": search,
        "total_spend": total_spend,
        "predicted_sales": predicted_sales,
        "roi": roi,
    }
