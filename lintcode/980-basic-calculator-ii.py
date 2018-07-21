class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """

    def calculate(self, s):
        # Write your code here
        if not s: return '0'
        stack, num, sign = [], 0, '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and not c.isspace()) or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                num, sign = 0, c
        return sum(stack)
