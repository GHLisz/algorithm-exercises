class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """

    def addDigits(self, num):
        # write your code here
        def sol1(num):
            if num == 0: return 0
            return (num - 1) % 9 + 1

        def sol2(num):
            while num // 10 > 0:
                total = 0
                while num > 0:
                    total += num % 10
                    num //= 10
                num = total
            return num

        return sol1(num)
