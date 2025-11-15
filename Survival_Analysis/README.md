# Telecom Customer Survival Analysis Overview

This repository presents a full survival analysis of telecom customer churn, focusing on estimating customer lifetime, identifying churn-driving factors, and evaluating CLV across service segments. The project uses an AFT modeling framework and includes both statistical findings and practical business recommendations.

---

## Dataset

The dataset (`telco.csv`) includes **1,000 telecom subscribers** and contains:

- **Demographic variables:** age, marital status, address duration  
- **Service-related features:** internet, voice, call forwarding  
- **Subscription plan type:** Basic, Plus, E-service, Total service  
- **Churn indicator and survival time**  

These variables were used to model customer retention and estimate CLV.

---

## Files in This Repository

- **`CLV.ipynb`** — Main notebook containing data exploration, survival modeling, CLV estimation, and churn-risk segmentation  
- **`report.md`** — Detailed findings and strategic recommendations  
- **`requirements.txt`** — Python dependencies needed to reproduce results  
- **`README.md`** — Project overview and instructions  

---

## Modeling Approach

The analysis includes:

- Data cleaning and feature preparation  
- Fitting multiple AFT models (Weibull, LogNormal, LogLogistic)  
- Selecting the **LogNormal AFT model** as the best-performing option  
- Interpreting coefficients using `exp(coef)` for lifetime effects  
- Estimating individual CLV using predicted survival times  
- Segmenting customers into **high-value** and **high-risk** groups  
- Retention budget estimation and strategic recommendations  

---

## Key Insights (Brief)

### Drivers of Churn Risk

- Service-related features (plan type, internet, voice services) are the strongest predictors of retention  
- Higher-tier plans and added services significantly extend customer lifetime  
- Some demographic factors (age, address duration) also support retention  
- Unmarried customers show higher churn risk  

### Most Valuable Customer Segments

- High-value customers (top 25% CLV) do **not** overlap with high-risk customers  
- Plus and E-service customers have the highest CLV and lowest churn  
- Basic customers show the highest churn risk  

### Retention Budget

- Annual revenue at risk: **$63,120.24**  
- 20% allocation suggests a recommended retention budget of **$12,624.05**  

---

## Recommended Strategies

Based on churn patterns and CLV results:

1. **Strengthen early-tenure onboarding**  
   - Churn risk is highest within the first 24 months  
   - Personalized onboarding or early engagement campaigns can help  

2. **Upgrade Basic service customers**  
   - This group has the highest churn probability  
   - Encourage upgrades to higher-tier plans with discounts or bundle offers  

3. **Target younger and unmarried customers**  
   - These groups are more likely to churn  
   - Provide tailored loyalty programs or promotional offers  

4. **Protect high-CLV customers**  
   - Offer perks, bundles, or proactive communication  
   - Especially for E-service customers without internet/voice services  

These actions help protect profitable customers and improve overall lifetime value.

---

## Setup and Usage

1. **Install dependencies**:

```bash
pip install -r requirements.txt
