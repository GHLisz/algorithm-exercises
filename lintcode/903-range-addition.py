class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """

    def getModifiedArray(self, length, updates):
        # Write your code here
        res = [0] * length
        if not updates: return res

        for update in updates:
            start, end, inc = update
            res[start] += inc
            if end < length - 1:
                res[end + 1] -= inc

        from itertools import accumulate
        return list(accumulate(res))
