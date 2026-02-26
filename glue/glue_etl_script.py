# AWS Glue ETL Script
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1771626681777 = glueContext.create_dynamic_frame.from_catalog(database="sentiment_db", table_name="aws_nlp_sentiment_tarun", transformation_ctx="AWSGlueDataCatalog_node1771626681777")

# Script generated for node Select Fields
SelectFields_node1771626694442 = SelectFields.apply(frame=AWSGlueDataCatalog_node1771626681777, paths=["name", "`reviews.text`", "`reviews.rating`"], transformation_ctx="SelectFields_node1771626694442")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SelectFields_node1771626694442, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1771624209585", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1771626779441 = glueContext.write_dynamic_frame.from_options(frame=SelectFields_node1771626694442, connection_type="s3", format="csv", connection_options={"path": "s3://aws-nlp-sentiment-tarun/processed/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1771626779441")

job.commit()
