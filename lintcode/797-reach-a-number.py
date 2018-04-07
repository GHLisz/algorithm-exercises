class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """

    def reachNumber(self, target):
        # Write your code here
        t, n, sum = abs(target), 0, 0

        while t > sum:
            n += 1
            sum += n

        if t == sum:
            return n

        rem = sum - target
        if (rem % 2) == 0:
            return n
        else:
            return n + 1 if (n % 2) == 0 else n + 2
