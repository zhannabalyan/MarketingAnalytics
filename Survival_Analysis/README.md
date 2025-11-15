# Telecom Customer Survival Analysis Overview

This repository presents a full survival analysis of telecom customer churn, focusing on estimating customer lifetime, identifying churn-driving factors, and evaluating CLV across service segments. The project uses an AFT modeling framework and includes both statistical findings and practical business recommendations.

---

## Dataset

The dataset(`telco.csv`) includes 1000 telecom subscribers and contains:

- **Demographic variables:** age, marital status, address duration  
- **Service-related features:** internet, voice, call forwarding  
- **Subscription plan type:** Basic, Plus, E-service, Total service  
- **Churn indicator and survival time**  

These variables were used to model customer retention and estimate CLV.

---

## Files in This Repository

- **`CLV.ipynb`** — Main notebook containing data exploration, preprocessing, survival modeling, CLV estimation, and churn-risk segmentation.  
- **`report.md`** — Detailed findings, insights and recommendations.  
- **`requirements.txt`** — Python dependencies needed to reproduce results.  
- **`README.md`** — Homework overview and instructions.  

---

## Modeling Approach

The analysis includes:

- Data cleaning and feature preparation  
- Fitting multiple AFT models (Weibull, LogNormal, LogLogistic)  
- Selecting the LogNormal AFT model as the best-performing option  
- Interpreting coefficients using `exp(coef)` for lifetime effects  
- Estimating individual CLV using predicted survival times  
- Segmenting customers into high-value and high-risk groups  
- Retention budget estimation and strategic recommendations  

---

## Key Insights 

### What drove Churn Risk

- Features related with service(plan type, internet, voice services) are the strongest predictors of retention.  
- Advanced plans and extra services significantly extend customer lifetime.
- Some demographic factors like age also support retention.  
- Unmarried customers show higher churn risk.  

### Most Valuable Customer Segments

- High-value customers(top 25% CLV) do not overlap with high-risk customers.  
- Plus and E-service customers have the highest CLV and lowest churn rate.  
- Basic customers show the highest churn risk.  

### Retention Budget

- Annual revenue at risk: **63120.24**  
- 20% allocation suggests a recommended retention budget of **12624.05**  

---

## Recommended Strategies

Based on churn patterns and CLV results:

1. **Strengthen early-tenure onboarding**  
   - Churn risk is highest within the first 24 months.  
   - Personalized onboarding or early engagement campaigns can help.  

2. **Upgrade Basic service customers**  
   - This group has the highest churn probability.  
   - Encourage upgrades to more advanced plans with discounts or bundle offers.  

3. **Target younger and unmarried customers**  
   - These groups are more likely to churn.  
   - Provide tailored loyalty programs or promotional offers.  

4. **Protect high-CLV customers**  
   - Offer perks, bundles, or proactive communication.  
   - Especially for E-service customers without internet or voice services.  

These actions help protect profitable customers and improve overall lifetime value.

---

## Setup and Usage

1. **Clone the repository** to your local machine.  
2. **Install dependencies** using:

```bash
pip install -r requirements.txt

Place the dataset in the project directory:

telco.csv


Launch and run the notebook:

jupyter notebook Survival_Analysis.ipynb

