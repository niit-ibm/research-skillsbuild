# Function to upload to Pinecone
def upload_to_pinecone(vector, metadata, id):
    index.upsert(vectors=[{
        'id': id,
        'values': vector,
        'metadata': metadata
    }])    
