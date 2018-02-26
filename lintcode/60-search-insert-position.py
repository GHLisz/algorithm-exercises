class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """

    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0

        start, end = 0, len(A) - 1

        while end - start > 1:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)
