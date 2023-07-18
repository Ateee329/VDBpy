from VDBpy.indexing import VectorIndex
from VDBpy.query import VectorQuery

def main():
    # Create a new vector index
    index = VectorIndex()

    # Add some vectors to the index
    index.add_vector([1, 2, 3], 'vector1')
    index.add_vector([4, 5, 6], 'vector2')

    # Create a new vector query
    query = VectorQuery(index)

    # Execute the query
    results = query.execute([2, 2, 2], k=2)

    '''
    # Execute the query using cosine similarity
    results = query.execute([2,2,2], k=2, metric='cosine')
    # Execute the query using Manhattan distance
    results = query.execute([2,2,2], k=2, metric='manhattan')
    # Execute the query using Jaccard similarity
    results = query.execute([2,2,2], k=2, metric='jaccard')
    '''
  
    # Print the results
    for id, similarity in results:
        print(f"ID: {id}, Similarity: {similarity}")

if __name__ == "__main__":
    main()

# When you run this script, it will print the IDs of the two vectors in the index that are most similar to the query vector. The similarity is calculated using the Euclidean distance by default, but you can change this by passing a different metric to the execute method. For example, to use cosine similarity, you could call query.execute([2, 2, 2], k=2, metric='cosine').
