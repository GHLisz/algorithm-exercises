class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """

    def reachNumber(self, target):
        # Write your code here
        target, k = abs(target), 0
        while target > 0:
            k += 1
            target -= k
        return k + 1 + k % 2 if target % 2 else k
