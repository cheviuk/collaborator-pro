def search(query_vector, country=None, language=None, budget=None):
    query = {
        "query": {
            "script_score": {
                "query": {
                    "bool": {
                        "filter": [
                            {"term": {"country": country}},
                            {"term": {"language": language}},
                            {"term": {"budget": budget}},

                        ]
                    }
                },
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'vector') + 1.0",
                    "params": {"query_vector": query_vector}
                }
            }
        },
        "size": 10
    }

    result = es.search(index="platforms", body=query)
    return result['hits']['hits']

# Search example
query_vector = get_embedding("купити пральну машину") # See bert example
results = search(query_vector, country="US", language="en")

# Show results
for hit in results:
    print(f"Score: {hit['_score']} | Document: {hit['_source']}")