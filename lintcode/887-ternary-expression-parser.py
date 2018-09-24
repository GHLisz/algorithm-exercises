class Solution:
    """
    @param expression: a string, denote the ternary expression
    @return: a string
    """

    def parseTernary(self, expression):
        # write your code here
        stk = []

        for i in range(len(expression) - 1, -1, -1):
            c = expression[i]
            if stk and stk[-1] == '?':
                stk.pop()
                first = stk.pop()
                stk.pop()
                second = stk.pop()
                stk.append(first if c == 'T' else second)
            else:
                stk.append(c)
        return stk[-1]
