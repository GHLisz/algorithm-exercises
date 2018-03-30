class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        # write your code here
        dic = collections.defaultdict(int)

        for arr in arrs:
            for a in arr:
                dic[a] += 1

        return sum(1 for v in dic.values() if v == len(arrs))
