class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        def recursive(s):
            def decode(s):
                nonlocal i
                res = ''
                while i < len(s) and s[i] != ']':
                    print('while', i)
                    if s[i].isdigit():
                        n = 0
                        while i < len(s) and s[i].isdigit():
                            n = n * 10 + int(s[i])
                            i += 1
                        i += 1  # '['
                        t = decode(s)
                        i += 1  # ']'
                        res += t * n
                    else:
                        res += s[i]
                        i += 1
                return res
            i = 0
            return decode(s)

        def iterative(s):
            stack, cur_num, cur_str = [], 0, ''
            for c in s:
                if c == '[':
                    stack.extend([cur_str, cur_num])
                    cur_str, cur_num = '', 0
                elif c == ']':
                    num = stack.pop()
                    pre_str = stack.pop()
                    cur_str = pre_str + num * cur_str
                elif c.isdigit():
                    cur_num = cur_num * 10 + int(c)
                else:
                    cur_str += c
            return cur_str

        return iterative(s)
