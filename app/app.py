from flask import Flask, render_template, request
import sys
import os

# allow importing from src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predict import predict_sales
from src.optimizer import optimize_budget

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html")

    tv = float(request.form["tv"])
    radio = float(request.form["radio"])
    social = float(request.form["social"])
    search = float(request.form["search"])
    price = float(request.form["price"])
    competitor = float(request.form["competitor"])

    predicted_sales = predict_sales(tv, radio, social, search, price, competitor)
    total_spend = tv + radio + social + search
    roi = round(((predicted_sales - total_spend) / total_spend) * 100, 2)

    return render_template(
        "result.html",
        prediction=predicted_sales,
        tv=tv,
        radio=radio,
        social=social,
        search=search,
        price=price,
        competitor=competitor,
        total_spend=total_spend,
        roi=roi,
    )


@app.route("/optimize", methods=["GET", "POST"])
def optimize():
    if request.method == "GET":
        return render_template("optimize.html")

    total_budget = float(request.form["total_budget"])
    price = float(request.form["price"])
    competitor = float(request.form["competitor"])

    result = optimize_budget(total_budget, price, competitor)
    roi = round(((result["predicted_sales"] - total_budget) / total_budget) * 100, 2)

    return render_template(
        "optimize_result.html",
        result=result,
        total_budget=total_budget,
        roi=roi,
    )


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        tv = float(request.form["tv"])
        radio = float(request.form["radio"])
        social = float(request.form["social"])
        search = float(request.form["search"])
        price = float(request.form["price"])
        competitor = float(request.form["competitor"])

        predicted_sales = predict_sales(tv, radio, social, search, price, competitor)
        total_spend = tv + radio + social + search
        roi = round(((predicted_sales - total_spend) / total_spend) * 100, 2)

        spend_data = [tv, radio, social, search]

        return render_template(
            "dashboard.html",
            total_spend=total_spend,
            predicted_sales=predicted_sales,
            roi=roi,
            spend_data=spend_data,
            no_data=False
        )

    # GET request → no data yet
    return render_template(
        "dashboard.html",
        no_data=True
    )


if __name__ == "__main__":
    app.run(debug=True)
