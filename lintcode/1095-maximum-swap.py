class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """

    def maximumSwap(self, num):
        # Write your code here
        digits = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(digits)}
        for i, x in enumerate(digits):
            for d in range(9, x, -1):
                if last.get(d, -float('inf')) > i:
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int(''.join(map(str, digits)))
        return num
