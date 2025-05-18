# RFM Customer Segmentation with PySpark

This project implements Recency, Frequency, and Monetary (RFM) customer segmentation using PySpark on Databricks.

##  Technologies
- PySpark
- Databricks (Community Edition)
- CSV data (sample)

## Use Case
Identify customer segments for targeted marketing campaigns based on transaction behavior.

## Sample Output
- RFM Score: `543`, `444`, `321`...
- Segment: Champions, At Risk, Loyal, etc.

## To Run
1. Upload `transactions.csv` in Databricks `/FileStore/tables/`
2. Load and run `rfm_pipeline.py`


df = spark.read.format("csv").option("header", True).load("/FileStore/tables/c1.csv")
df.show()
from pyspark.sql import functions as F
from pyspark.sql.window import Window
# Load CSV with uploaded file path
df = spark.read.format("csv").option("header", True).load("/FileStore/tables/c1.csv") \
    .withColumn("amount", F.col("amount").cast("double")) \
    .withColumn("transaction_date", F.to_date("transaction_date", "yyyy-MM-dd"))
# Reference date: latest transaction date
ref_date = df.agg(F.max("transaction_date")).first()[0]
# Step 1: RFM calculation
rfm_df = df.groupBy("customer_id").agg(
    F.max("transaction_date").alias("last_purchase_date"),
    F.count("transaction_id").alias("frequency"),
    F.sum("amount").alias("monetary")
).withColumn(
    "recency", F.datediff(F.lit(ref_date), F.col("last_purchase_date"))
).select("customer_id", "recency", "frequency", "monetary")

# Step 2: Scoring using quantiles
rfm_scored = rfm_df.withColumn("r_score", F.ntile(5).over(Window.orderBy("recency"))) \
    .withColumn("f_score", F.ntile(5).over(Window.orderBy(F.desc("frequency")))) \
    .withColumn("m_score", F.ntile(5).over(Window.orderBy(F.desc("monetary"))))
    
# Step 3: RFM score and segment
rfm_final = rfm_scored.withColumn("rfm_score", F.concat_ws("", F.col("r_score"), F.col("f_score"), F.col("m_score")))

# Segment labeling
def rfm_segment(score):
    if score >= "444":
        return "HIGH"
    elif score >= "344":
        return "MEDIUM"
    elif score >= "244":
        return "LOW"
    else:
        return "At Risk"

rfm_segment_udf = F.udf(rfm_segment)
rfm_labeled = rfm_final.withColumn("segment", rfm_segment_udf(F.col("rfm_score")))
# Final output
display(rfm_labeled.select("customer_id", "recency", "frequency", "monetary", "rfm_score", "segment"))
