class Solution:
    """
    @param: num: An integer
    @return: An integer
    """

    def countOnes(self, num):
        # write your code here
        def ac(num):
            total = 0
            for i in range(32):
                total += num & 1
                num >>= 1
            return total

        def countOnes1(num):  # Wrong Answer
            count = 0
            while num != 0:
                if num % 2 == 1:
                    count += 1
                num /= 2
            return count

        def countOnes2(num):  # Time Limit Exceeded
            count = 0
            while num != 0:
                count += num & 0x01
                num = num >> 1
            return count

        def countOnes3(num):  # Time Limit Exceeded
            count = 0
            while num != 0:
                num = num & (num - 1)
                count += 1
            return count

        return ac(num)
