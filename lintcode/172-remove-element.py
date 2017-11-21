class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        i, pointer = 0, len(A) - 1
        while i <= pointer:
            if A[i] == elem:
                A[i] = A[pointer]
                pointer -= 1
            else:
                i += 1
        return pointer + 1
