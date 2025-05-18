# 🧠 RFM Customer Segmentation using PySpark on Databricks

This project demonstrates how to perform **RFM (Recency, Frequency, Monetary) customer segmentation** using **PySpark** in **Azure Databricks**. 
It is designed as a scalable and cloud-agnostic solution for marketing and business analytics teams to identify high-value and at-risk customers from transactional data.

---

##  Overview

In this project, we:
- Processed customer transaction data using **PySpark**
- Calculated **RFM metrics**:  
  - **Recency** – Days since last purchase  
  - **Frequency** – Number of purchases  
  - **Monetary** – Total purchase amount
- Scored customers using quantile-based bucketing
- Assigned customers to segments such as `HIGH`, `MEDIUM`,'LOW', `At Risk`
- Built the pipeline to scale across large datasets in cloud platforms

---

## Business Use Case

> Marketing teams often need to tailor campaigns to specific customer groups.  
> Using RFM segmentation allows them to:
> - Retain high-value customers
> - Re-engage at-risk or lapsed customers
> - Design cost-efficient, targeted offers

This project helped reduce churn and increase ROI in real-world applications.

---

## Tech Stack

- **PySpark** (Spark DataFrame API)
- **Databricks** (Azure, but portable to AWS or GCP)
- **CSV** input file with transactional data


---

## 📂 Folder Structure

rfm-customer-segmentation/
├── rfm_pipeline.py # Main PySpark logic
├── transactions.csv # Sample input data
├── rfm_output.png # Sample visual output
└── README.md # Project description



---
 Example Output

| customer_id | recency | frequency | monetary | rfm_score | segment    |
|-------------|---------|-----------|----------|-----------|------------|
| C123        | 12      | 8         | 560.00   | 545       | HIGH  |
| C456        | 78      | 2         | 120.50   | 231       | At Risk    |
| C789        | 25      | 5         | 320.90   | 443       | MEDIUM     |

---

## How to Run

1. **Upload `transactions.csv`** to Databricks under `/FileStore/tables/`
2. **Create a notebook** and paste `rfm_pipeline.py` code
3. **Run all cells** to view the final segmented DataFrame
4. Visualize in Databricks UI or export results

---

## Key Learnings

- Working with PySpark for real-world feature engineering
- Applying analytical models in distributed environments
- Creating reusable and cloud-agnostic pipelines
- Business translation of technical models (RFM → revenue impact)

---

##  Author

**Aishwarya Deshmukh**  
Data Engineer | Azure + PySpark | Analytics Enthusiast  
📧 aishadeshmukh105@gmail.com
