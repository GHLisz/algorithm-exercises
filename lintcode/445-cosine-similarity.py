class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Cosine similarity
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        if len(A) != len(B):
            return 2

        n = len(A)
        up = 0
        for i in range(n):
            up += A[i] * B[i]
        down = sum(a * a for a in A) * sum(b * b for b in B)
        if down == 0:
            return 2
        return up / (down ** 0.5)
