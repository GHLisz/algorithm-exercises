class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """

    def repeatedStringMatch(self, A, B):
        # write your code here
        def sol1():
            from math import ceil
            times = ceil(len(B) / len(A))
            for i in range(2):
                if B in (A * (times + i)):
                    return times + i
            return -1

        def sol2():
            from math import ceil
            kmp = [0] * (len(B) + 1)
            
            i, j = 1, 0
            while i < len(B):
                if B[j] == B[i]:
                    j += 1
                    kmp[i] = j
                    i += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = kmp[j - 1]

            i, j = 0, 0
            while i < len(B):
                while j < len(B) and A[(i + j) % len(A)] == B[j]:
                    j += 1
                if j == len(B):
                    return ceil((i + j) / len(A))
                i += 1
                j = kmp[j - 1]

            return -1

        return sol2()
