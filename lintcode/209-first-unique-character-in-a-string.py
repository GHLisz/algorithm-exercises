class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        c = collections.Counter(str)
        for v in str:
            if c[v] == 1:
                return v
        return None
