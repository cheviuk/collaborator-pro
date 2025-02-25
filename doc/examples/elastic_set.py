from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

# Сreate mapping for vector
index_mapping = {
    "mappings": {
        "properties": {
            "platform": {"type": "text"},
            "language": {"type": "text"},
            "price": {"type": "text"},
            "vector": {
                "type": "dense_vector",
                "dims": 768,  # Size of BERT-vector
                "index": True,
                "similarity": "cosine"
            }
        }
    }
}

# Create index (just once)
es.indices.create(index="my_index", body=index_mapping)

# Document example
document = {
    "platform": "domain.com",
    "link": "domain.com/...",
    "language": "EN",
    "budget": "1000000"
    "vector": vector # See bert.py
}

# Document indexation
es.index(index="platforms", document=document)