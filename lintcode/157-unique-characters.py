class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique(self, str):
        # write your code here
        from collections import Counter

        return all(n == 1 for n in Counter(str).values())
