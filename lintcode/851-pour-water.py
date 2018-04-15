class Solution:
    """
    @param heights: the height of the terrain
    @param V: the units of water
    @param K: the index
    @return: how much water is at each index
    """

    def pourWater(self, heights, V, K):
        # Write your code here
        def drop(h, k):
            best = k
            for d in (-1, 1):
                i = k + d
                while 0 <= i < len(h) and h[i] <= h[i - d]:
                    if h[i] < h[best]:
                        best = i
                    i += d
                if best != k:
                    break
            heights[best] += 1

        for _ in range(V):
            drop(heights, K)
        return heights
