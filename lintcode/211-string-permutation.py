class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        # write your code here
        if len(A) != len(B):
            return False

        m = [0 for _ in range(256)]
        for c in A:
            m[ord(c)] += 1
        for c in B:
            m[ord(c)] -= 1
            if m[ord(c)] < 0:
                return False
        return True
