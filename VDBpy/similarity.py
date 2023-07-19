import math
from collections import Counter

def dot(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def cosine_similarity(v1, v2):
    dot_product = sum(x * y for x, y in zip(v1, v2))
    magnitude1 = math.sqrt(sum(x ** 2 for x in v1))
    magnitude2 = math.sqrt(sum(y ** 2 for y in v2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

def euclidean_distance(v1, v2):
    # Compute the Euclidean distance between two vectors
    distance = 0
    for i in range(len(v1)):
        distance += (v1[i] - v2[i]) ** 2
    return math.sqrt(distance)

def manhattan_distance(v1, v2):
    distance = 0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])
    return distance

'''   
def jaccard_similarity(list1,list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    intersection = len(list((c1&c2).elements()))
    union = len(list((c1|c2).elements()))
    if union == 0:
        return 1.0 # both lists are empty, so the Jaccard similarity is 1.0
    return intersection / union
'''
