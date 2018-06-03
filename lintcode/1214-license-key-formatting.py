class Solution:
    """
    @param S: a string
    @param K: a integer
    @return: return a string
    """
    def licenseKeyFormatting(self, S, K):
        # write your code here
        S = S.replace("-", "").upper()[::-1]
        return '-'.join([S[i:i+K] for i in range(0, len(S), K)])[::-1]
