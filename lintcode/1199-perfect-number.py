class Solution:
    """
    @param num: an integer
    @return: returns true when it is a perfect number and false when it is not
    """

    def checkPerfectNumber(self, num):
        # write your code here
        if num <= 0: return False

        total, i = 0, 1
        while i * i <= num:
            if num % i == 0:
                total += i
                if i * i != num:
                    total += num // i
            i += 1

        return total - num == num
