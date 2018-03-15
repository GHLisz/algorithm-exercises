class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        # Write your code here
        dic = {}
        for i, b in enumerate(B):
            dic[b] = i
        return [dic[a] for a in A]
