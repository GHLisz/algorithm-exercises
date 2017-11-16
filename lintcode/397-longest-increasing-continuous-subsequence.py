class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if not A:
            return 0

        in_count, de_count, result = 1, 1, 1

        i, n = 1, len(A)

        while i != n:
            if A[i] >= A[i - 1]:
                in_count += 1
                de_count = 1
                result = max(result, in_count)
            else:
                de_count += 1
                in_count = 1
                result = max(result, de_count)
            i += 1

        return result
