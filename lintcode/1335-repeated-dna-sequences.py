class Solution:
    """
    @param s: a string
    @return: return List[str]
    """

    def findRepeatedDnaSequences(self, s):
        # write your code here
        seen, repeated = set(), set()
        for i in range(len(s) - 9):
            sub = s[i:i + 10]
            if sub in seen:
                repeated.add(sub)
            seen.add(sub)
        return list(repeated)
