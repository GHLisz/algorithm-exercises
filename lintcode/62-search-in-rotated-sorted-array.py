class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        l, h = 0, len(A) - 1
        while l <= h:
            m = (l + h) // 2
            if A[m] == target:
                return m
            elif (A[m] > A[l] and A[m] > target >= A[l]) \
                    or (A[m] < A[l] and not (A[h] >= target > A[m])):
                h = m - 1
            else:
                l = m + 1
        return -1
