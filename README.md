AI Marketing Mix Model & ROI Optimization Dashboard

A data-driven web application that predicts sales based on multi-channel marketing spend and recommends the most efficient budget allocation to maximize ROI.

1️⃣ Project Overview

Marketing teams continually invest in channels like TV, Radio, Social Media, and Search Ads—yet it remains difficult to determine:

Which channels actually drive sales

How much each channel contributes

What the ideal budget allocation should be

How competitor activity impacts revenue

This project solves that challenge using:

 Marketing Mix Modeling (MMM)
 Diminishing-returns based optimization logic
 An interactive, business-friendly dashboard

The system helps decision-makers to:

Estimate sales for any media plan

Understand multi-channel impact

Optimize the budget for maximum ROI

Support strategic media planning with evidence

2️⃣ Business Value
Marketing & Growth Teams

Evaluate spend effectiveness

Compare alternative budget scenarios

Identify high-performing channels

Leadership & Strategy

Estimate revenue impact before launching campaigns

Choose the most cost-efficient media mix

Reduce spend wastage and boost ROI

Business Analysts

Convert raw budget data into revenue insights

Understand diminishing returns

Support strategic decisions with a dashboard

3️⃣ Techniques & Tools Used
Modeling Approach

Ridge Regression (stable + handles multicollinearity)

Log-transformed features to model diminishing returns

Channel-level ROI optimization using marginal ROI logic

Tech Stack

Python

Flask (web application)

Pandas

Scikit-Learn

Bootstrap 5 (UI)

Chart.js (visualizations)

4️⃣ Example Output
Input Media Plan
Channel	Spend (₹)
TV	25,000
Radio	22,000
Social	19,000
Search	25,000
Total Spend	₹91,000

Additional Inputs:

Product Price: ₹120

Competitor Spend: ₹15,000

Model Output

Predicted Sales: ₹4,75,200.06

ROI: 422.2%

Insights:
TV and Search show stronger marginal contribution, indicating higher ROI potential at scale.

5️⃣ Key Features of the Dashboard
📈 Sales Predictor

Input channel spend → get

Predicted sales

Total spend

ROI

Dashboard visualization

🎯 Budget Optimizer

Input only total budget → system recommends

Optimized TV/Radio/Social/Search allocation

Expected sales

ROI

Visualization + dashboard export

📊 Dashboard View

KPI cards (Spend, Sales, ROI)

Channel distribution pie chart

Clean, business-focused interface

6️⃣ Project Structure
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

7️⃣ Skills Demonstrated
Data & Modeling Skills

Marketing Mix Modeling (MMM)

Regression modeling

Optimization algorithms

ROI computation

Business Analysis Skills

Translating data into business decisions

Understanding marketing KPIs

Scenario-based planning

Dashboard storytelling

Development Skills

Flask application development

UI/UX design with Bootstrap

Chart-based visualization

End-to-end project structuring

8️⃣ Author

Hephzibah Paul
Business Analyst | Data & AI Enthusiast