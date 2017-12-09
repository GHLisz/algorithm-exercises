class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        res = [-1, -1]
        if len(A) == 0:
            return res

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            res[0] = start
        elif A[end] == target:
            res[0] = end
        else:
            return res

        start, end = res[0], len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        res[1] = end if A[end] == target else start

        return res
