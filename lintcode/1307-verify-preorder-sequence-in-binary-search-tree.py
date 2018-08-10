class Solution:
    """
    @param preorder: List[int]
    @return: return a boolean
    """

    def verifyPreorder(self, preorder):
        # write your code here
        def sol1():
            low, stack = -float('inf'), []
            for a in preorder:
                if a < low: return False
                while stack and a > stack[-1]:
                    low = stack.pop()
                stack.append(a)
            return True

        def sol2():
            low, i = -float('inf'), -1
            for a in preorder:
                if a < low: return False
                while i >= 0 and a > preorder[i]:
                    low = preorder[i]
                    i -= 1
                i += 1
                preorder[i] = a
            return True

        return sol2()
