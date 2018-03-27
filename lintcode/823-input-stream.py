class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """

    def inputStream(self, inputA, inputB):
        # Write your code here
        def get_stat(stream):
            lis, length = [], 0
            for c in stream:
                if c == "<":
                    if length > 0:
                        lis.pop()
                        length -= 1
                else:
                    lis.append(c)
                    length += 1
            return lis, length

        a, _ = get_stat(inputA)
        b, _ = get_stat(inputB)

        return "YES" if a == b else "NO"
