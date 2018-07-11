class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Cosine similarity
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        if len(A) != len(B): return 2
        up = sum(a * b for a, b in zip(A, B))
        down = sum(map(lambda x: x * x, A)) * sum(map(lambda x: x * x, B))
        return up / (down ** 0.5) if down else 2
