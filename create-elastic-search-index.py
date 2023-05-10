from elasticsearch import Elasticsearch
import os

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# directory path
dir_path = "/path/to/git/repository/"

# Traverse the directory tree and extract information from each file
def process_directory(path):
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            process_directory(filepath)
        else:
            with open(filepath, 'r') as f:
                content = f.read()
                # Extract relevant information from the file
                # Format the extracted information into a JSON document
                json_doc = {
                    "filename": filename,
                    "content": content,
                    "metadata": {
                        "category": os.path.basename(path),
                        "subcategory": os.path.basename(os.path.dirname(path))
                    }
                }
                # Send the JSON document to Elastic Search index
                es.index(index='git_repo', body=json_doc)

# Traverse the directory tree starting from the root directory
process_directory(dir_path)
