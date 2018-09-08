class Solution:
    """
    @param num: a string
    @return: Is it a valid additive number
    """

    def isAdditiveNumber(self, num):
        # Write your code here
        def sol1():  # dfs, O(n^3)
            def dfs(num, i, j, k):  # start from [i, j) and [j, k)
                num1, num2 = int(num[i:j]), int(num[j:k])
                addition = str(num1 + num2)

                if not num.startswith(addition, k): return False
                if k + len(addition) == len(num): return True
                return dfs(num, j, k, k + len(addition))

            for i in range(1, len(num) // 2 + 1):
                if num[0] == '0' and i > 1: continue
                for j in range(i + 1, len(num)):
                    if num[i] == '0' and j - i > 1: continue
                    if dfs(num, 0, i, j): return True
            return False

        def sol2():
            from itertools import combinations

            n = len(num)
            for i, j in combinations(range(1, n), 2):
                a, b = num[:i], num[i:j]
                if b != str(int(b)):
                    continue
                while j < n:
                    c = str(int(a) + int(b))
                    if not num.startswith(c, j):
                        break
                    j += len(c)
                    a, b = b, c
                if j == n:
                    return True
            return False

        return sol1()
