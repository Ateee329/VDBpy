from VDBpy.similarity import euclidean_distance, cosine_similarity, manhattan_distance #, jaccard_similarity

class VectorIndex:
    def __init__(self):
        self.vectors = {}
        self.ids = []
    
    def add_vector(self, vector, id):
        self.vectors[id] = vector
        self.ids.append(id)
    
    def search(self,query_vector,k=10,metric='euclidean'):
        # Use the specified similarity metric to find the k most similar vectors to the query vector
        if metric == 'euclidean':
            similarities = [euclidean_distance(query_vector,v) for v in self.vectors.values()]
        elif metric == 'cosine':
            similarities = [cosine_similarity(query_vector,v) for v in self.vectors.values()]
        elif metric == 'manhattan':
            similarities = [manhattan_distance(query_vector,v) for v in self.vectors.values()]
        # elif metric == 'jaccard':
            # similarities = [jaccard_similarity(query_vector,self.vectors[id]) for id in self.ids]
        else:
            raise ValueError('Unsupported similarity metric: ' + metric)

        sorted_indices = sorted(range(len(similarities)), key=lambda k: similarities[k], reverse=metric=='cosine')
        return [(self.ids[i], similarities[i]) for i in sorted_indices[:k]]
    