class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        # write your code here
        sub_max, total = -float('inf'), 0
        start, end = 0, -1
        res = [-1, -1]

        for n in A:
            if total < 0:
                total = n
                start = end + 1
                end = start
            else:
                total += n
                end += 1
            if total > sub_max:
                sub_max = total
                res = [start, end]

        return res
