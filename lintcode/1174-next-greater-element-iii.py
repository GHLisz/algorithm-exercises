class Solution:
    """
    @param n: an integer
    @return: the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n
    """

    def nextGreaterElement(self, n):
        # Write your code here
        chars = list(str(n))

        for i in range(len(chars) - 1, 0, -1):
            if chars[i] > chars[i - 1]:
                break
        else:
            return -1

        for j in range(len(chars) - 1, i - 1, -1):
            if chars[j] > chars[i - 1]:
                chars[j], chars[i - 1] = chars[i - 1], chars[j]
                break

        chars[i:] = sorted(chars[i:])
        res = int(''.join(chars))
        return -1 if res > 2 ** 31 - 1 else res
