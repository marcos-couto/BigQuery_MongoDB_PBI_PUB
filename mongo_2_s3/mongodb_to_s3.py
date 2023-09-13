import pymongo
import boto3
import json
from bson import Decimal128, ObjectId
import os

def lambda_handler(event, context):
    # Define OS path
    json_file_name = <File>  # Replace with your file
    json_file_path = os.path.join('/tmp', json_file_name)

    # Custom JSON encoder to handle Decimal128 serialization
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Decimal128):
                return str(o)
            if isinstance(o, ObjectId):
                return str(o)
            return super().default(o)

    # MongoDB Atlas connection string
    mongo_uri = "mongodb+srv://< user >:< password >< mongodb address server>"  # Replace with your MongoDB connection URL

    # AWS S3 credentials
    aws_access_key_id = '<aws_access_key_id>' # Replace with your aws_access_key_id
    aws_secret_access_key = '<aws_secret_access_key>' # Replace with your aws_secret_access_key
    aws_bucket_name ='<aws_bucket_name>' # Replace with your aws_bucket_name

    # MongoDB Atlas database and collection name
    mongo_db_name = '<mongo_db_name>'  # Replace with your mongo_db_name
    mongo_collection_name = '<mongo_collection_name>'  # Replace with your mongo_collection_name

    # Connect to MongoDB Atlas
    mongo_client = pymongo.MongoClient(mongo_uri)
    mongo_db = mongo_client[mongo_db_name]
    mongo_collection = mongo_db[mongo_collection_name]
    mongo_data = list(mongo_collection.find())

    # Export the collection data to a JSON file
    #json_file_path = 'TB02_01.json'
    with open(json_file_path, 'w') as f:
        json.dump(mongo_data, f, cls=CustomJSONEncoder)

    # Connect to AWS S3
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Upload the JSON file to S3
    with open(json_file_path, 'rb') as f:
        s3_client.upload_fileobj(f, aws_bucket_name, '<mongo_collection_name>') # Replace with your mongo_collection_name

    # Close the MongoDB connection
    mongo_client.close()

    return {
        "statusCode": 200,
        "body": json.dumps("Data inserted successfully!")
    }