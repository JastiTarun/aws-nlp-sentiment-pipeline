# AWS NLP Sentiment Analysis Pipeline

An end-to-end AWS data engineering and machine learning pipeline that processes Amazon product reviews and performs batch sentiment inference using managed cloud services.

---

## 🚀 Architecture Overview

View Architecture Diagram:  
[Open Architecture Diagram](architecture/aws-sentiment-pipeline-architecture.png)

This project implements a cloud-native pipeline integrating data engineering, machine learning, and analytics services on AWS.

---

## ☁️ Services Used

- Amazon S3 (Raw, Processed, Predictions storage)
- AWS Glue Crawler
- AWS Glue ETL Jobs
- Amazon SageMaker (Batch Sentiment Inference)
- Amazon Athena
- Amazon QuickSight

---

## 🔄 Pipeline Flow

1. Raw Amazon reviews stored in Amazon S3  
2. AWS Glue Crawler performs schema discovery  
3. AWS Glue ETL job cleans and transforms review data  
4. Processed data written back to S3  
5. Amazon SageMaker performs batch sentiment inference using a transformer-based model  
6. Prediction outputs stored in S3  
7. Amazon Athena queries sentiment prediction results  
8. Amazon QuickSight visualizes insights through an interactive dashboard  

---

## 📊 Dashboard

View Dashboard :  
[Open QuickSight Dashboard](dashboard/quicksight-dashboard.png)

This dashboard provides:

- Sentiment distribution across reviews  
- Rating vs sentiment correlation  
- Products generating highest negative sentiment  

---

## 🤖 SageMaker Inference Notebook

Access the notebook used for sentiment prediction:  
[Open SageMaker Notebook](notebook/sagemaker_sentiment_inference.ipynb)

---

## 🧩 Glue ETL Script

View the AWS Glue ETL transformation logic:  
[Open Glue ETL Script](glue/glue_etl_script.py)

---

## 📊 Output & Insights

- Sentiment distribution across product reviews  
- Correlation between ratings and sentiment predictions  
- Identification of products generating highest negative sentiment  
- Interactive BI dashboard built in QuickSight  

---

## 🧠 Skills Demonstrated

- Data lake architecture design  
- ETL orchestration using AWS Glue  
- Serverless analytics with Athena  
- Batch ML inference using SageMaker  
- Cloud-native data visualization  
- AWS IAM and permission configuration  

---

## 📌 Use Case

Designed as a scalable cloud-native analytics pipeline for e-commerce review analysis, enabling businesses to monitor customer sentiment, identify product issues, and support data-driven decision-making.
