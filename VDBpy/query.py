class VectorQuery:

    def __init__(self, index):
        self.index = index

    def execute(self, query_vector, k=10):
        return self.index.search(query_vector, k)
    