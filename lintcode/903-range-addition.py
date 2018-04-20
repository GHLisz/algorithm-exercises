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
            res[update[0]] += update[2]
            if update[1] < length - 1:
                res[update[1] + 1] -= update[2]

        from itertools import accumulate
        res = list(accumulate(res))
        return res
