AI Marketing Mix Model & ROI Optimization Dashboard

A data-driven web application that predicts sales based on multi-channel marketing spend and recommends the most efficient budget allocation to maximize ROI.

1️⃣ Project Overview

Marketing teams constantly invest in channels like TV, Radio, Social Media, and Search Ads—but it’s not always clear which channel contributes the most to sales or how budgets should be distributed.

This project solves that problem by combining Marketing Mix Modeling (MMM) with an ROI-driven optimization engine and a clean Flask-based dashboard.

The goal is to give decision-makers a simple, visual way to:

Estimate sales for any planned marketing spend

Understand channel contribution

Optimize the budget for maximum return

Support strategic media planning

2️⃣ Business Value

This system enables:

Marketing & Growth Teams

Evaluate spend effectiveness

Compare different budget plans

Understand diminishing returns across channels

Leadership & Strategy Teams

Estimate revenue impact before campaigns launch

Identify the most cost-effective channels

Make confident budget allocation decisions

Business Analysts

Translate media spend into revenue forecasts

Analyze competitor pressure

Build insights using a clear dashboard

3️⃣ Techniques & Tools

Modeling Approach:

Ridge Regression (stable and robust)

Log transforms to capture diminishing returns

Marginal ROI–based budget allocation algorithm

Tech Stack:

Python

Flask

Pandas

Scikit-learn

Bootstrap 5

Chart.js

4️⃣ Example Output

Using the following media plan:

Channel	Spend (₹)
TV	25,000
Radio	22,000
Social	19,000
Search	25,000
Total Spend	₹91,000

Additional Inputs:

Product Price: ₹120

Competitor Spend: ₹15,000

Model Prediction:

Predicted Sales: ₹4,75,200.06

ROI: 422.2%

This scenario suggests that TV and Search are likely delivering higher incremental value compared to other channels.

5️⃣ Key Features of the Dashboard
Sales Predictor

Enter marketing spend → get immediate sales forecast + ROI.

Budget Optimizer

Enter total budget → get recommended allocation across channels.

Dashboard View

KPI cards (Spend, Sales, ROI)

Spend distribution pie chart

Clear explanations for business users

6️⃣ Project Structure

```
marketing-mix-optimizer/
│
├── app/
│   ├── app.py
│   └── templates/
│       ├── index.html
│       ├── dashboard.html
│       ├── predict.html
│       ├── result.html
│       ├── optimize.html
│       └── optimize_result.html
│
├── src/
│   ├── train_model.py
│   ├── predict.py
│   └── optimizer.py
│
├── data/
│   └── marketing_data.csv
│
├── requirements.txt
├── LICENSE
└── README.md
```


7️⃣ Skills Demonstrated

Marketing Mix Modeling

Regression modeling and evaluation

Business analytics & ROI interpretation

Flask application development

Creating dashboards for business users

Translating data science into decisions

8️⃣ Author

Hephzibah Paul
Business Analyst | Data & AI Enthusiast