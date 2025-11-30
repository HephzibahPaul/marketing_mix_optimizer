from src.predict import predict_sales


def marginal_roi(tv, radio, social, search, price, competitor, delta=1000):
    """
    Marginal ROI: extra sales for +₹delta spend in each channel.
    Uses the safe MMM model under the hood.
    """
    base = predict_sales(tv, radio, social, search, price, competitor)

    roi_tv = predict_sales(tv + delta, radio, social, search, price, competitor) - base
    roi_radio = predict_sales(tv, radio + delta, social, search, price, competitor) - base
    roi_social = predict_sales(tv, radio, social + delta, search, price, competitor) - base
    roi_search = predict_sales(tv, radio, social, search + delta, price, competitor) - base

    return {
        "tv": roi_tv / delta,
        "radio": roi_radio / delta,
        "social": roi_social / delta,
        "search": roi_search / delta,
    }


def optimize_budget(total_budget, price, competitor, steps=20):
    """
    Allocate budget in 'steps' chunks to the channel
    with the highest marginal ROI based on MMM.
    """
    tv = radio = social = search = 0.0
    chunk = total_budget / steps

    for _ in range(steps):
        rois = marginal_roi(tv, radio, social, search, price, competitor)
        best_channel = max(rois, key=rois.get)

        if best_channel == "tv":
            tv += chunk
        elif best_channel == "radio":
            radio += chunk
        elif best_channel == "social":
            social += chunk
        else:
            search += chunk

    predicted = predict_sales(tv, radio, social, search, price, competitor)

    return {
        "tv": round(tv, 2),
        "radio": round(radio, 2),
        "social": round(social, 2),
        "search": round(search, 2),
        "predicted_sales": predicted,
    }
