class Solution:
    """
    @param source: List[str]
    @return: return List[str]
    """

    def removeComments(self, source):
        # write your code here
        def sol1():  # regex
            import re
            return list(filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n')))

        def sol2():
            res, in_block = [], False
            for line in source:
                i = 0
                if not in_block:
                    newline = []
                while i < len(line):
                    if line[i:i + 2] == '/*' and not in_block:
                        in_block = True
                        i += 1
                    elif line[i:i + 2] == '*/' and in_block:
                        in_block = False
                        i += 1
                    elif not in_block and line[i:i + 2] == '//':
                        break
                    elif not in_block:
                        newline.append(line[i])
                    i += 1
                if newline and not in_block:
                    res.append(''.join(newline))
            return res

        return sol2()
