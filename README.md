# AWS NLP Sentiment Analysis Pipeline

An end-to-end AWS data engineering + ML pipeline that processes Amazon reviews and performs batch sentiment inference using managed cloud services.

---

## Architecture Overview

![Architecture](architecture/aws-sentiment-pipeline-architecture.png)

---

## Services Used

- Amazon S3 (Raw, Processed, Predictions)
- AWS Glue Crawler
- AWS Glue ETL Jobs
- Amazon SageMaker (Batch Inference)
- Amazon Athena
- Amazon QuickSight

---

## Pipeline Flow

1. Raw Amazon reviews stored in S3
2. Glue Crawler performs schema discovery
3. Glue ETL job cleans and transforms data
4. Processed data stored in S3
5. SageMaker runs batch sentiment inference
6. Predictions stored in S3
7. Athena queries prediction results
8. QuickSight dashboard visualizes insights

---

## Output

- Sentiment distribution analysis
- Rating vs Sentiment correlation
- Top products with negative sentiment
- Interactive BI dashboard in QuickSight

---

## Skills Demonstrated

- Data Lake architecture
- ETL orchestration
- Serverless analytics
- Managed ML inference
- Cloud data visualization
- AWS IAM & permissions handling

---

## Use Case

Designed as a scalable cloud-native analytics pipeline for e-commerce review analysis.

---
