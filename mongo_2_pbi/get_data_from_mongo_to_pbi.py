from pymongo import MongoClient
import pandas as pd

def get_documents_from_db(atlas_string, cluster_name, collection_name, n_documents):
    cluster = MongoClient(atlas_string)
    db = cluster[cluster_name]
    collection = db[collection_name]
    documents = collection.find(limit=n_documents)
    return list(documents)

atlas_string =   "mongodb+srv://< user >:< password >< mongodb address server>"  # Replace with your MongoDB connection URL
table_name = <MongoDB collection name> # Replace with your MongoDB tablename

# Replace with your quantity of documents
n_documents = <quantity of documents>

collection_name = table_name
# Replace with your MongoDB database name
n_documents = get_documents_from_db (atlas_string, <MongoDB database>, collection_name, n_documents)
collection name = pd.DataFrame(documents) # Replace with your MongoDB collection name
