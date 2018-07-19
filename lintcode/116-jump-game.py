class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        reach = 0
        for i in range(len(A)):
            if i > reach: return False
            reach = max(reach, i + A[i])
        return True
