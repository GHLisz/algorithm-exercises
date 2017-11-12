class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        showed_nums = set()
        while True:
            showed_nums.add(n)
            n = sum([int(x) ** 2 for x in list(str(n))])
            if n == 1 or n in showed_nums:
                break
        return n == 1
