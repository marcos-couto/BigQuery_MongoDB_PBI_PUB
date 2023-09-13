from google.cloud import bigquery
import json
import os
from pymongo import MongoClient

def lambda_handler(event, context):

    # Retrieve BigQuery credentials from environment variable
    bigquery_credentials = os.environ.get(< BIGQUERY CREDENTIALS >)  # Replace with your BigQuery Credentials

    # Initialize BigQuery client with credentials
    bigquery_client = bigquery.Client.from_service_account_info(json.loads(bigquery_credentials))
    # Initialize MongoDB client and connect to your MongoDB instance
    mongo_client = MongoClient( "mongodb+srv://< user >:< password >< mongodb address server>" )  # Replace with your MongoDB connection URL
    db = mongo_client[< MongoDB Database name>]  # Replace with your MongoDB database name
    collection = db[< MongoDB collection name >]  # Replace with your MongoDB collection name

    # Define your BigQuery SQL query

    # Replace with your project name, dataset name and table
    query = """
        SELECT * FROM `< Project name >.< Dataset name >.< Table >`"""

    # Run the BigQuery query
    query_job = bigquery_client.query(query)

    # Iterate through the query results and insert into MongoDB
    collection.insert_many([dict(x) for x in query_job])

    # Close the MongoDB connection
    mongo_client.close()

    # Return a response
    return {
        "statusCode": 200,
        "body": json.dumps("Data inserted successfully!")
    }


