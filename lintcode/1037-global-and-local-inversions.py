class Solution:
    """
    @param A: an array
    @return: is the number of global inversions is equal to the number of local inversions
    """

    def isIdealPermutation(self, A):
        # Write your code here
        def sol1():
            if len(A) <= 2: return True
            max_so_far = -1
            for i in range(len(A) - 2):
                max_so_far = max(max_so_far, A[i])
                if max_so_far > A[i + 2]: return False
            return True

        def sol2():
            for i in range(len(A)):
                if abs(A[i] - i) >= 2: return False
            return True

        return sol2()
