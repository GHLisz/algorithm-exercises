class Solution:
    """
    @param: num: An integer
    @return: An integer
    """

    def countOnes(self, num):
        # write your code here
        # return self.countOnes1(num) # 387 ms
        # return self.countOnes2(num) # 418 ms
        return self.countOnes3(num)  # 398 ms

    def countOnes1(self, num):
        count = 0
        while num != 0:
            if num % 2 == 1:
                count += 1
            num /= 2
        return count

    def countOnes2(self, num):
        count = 0
        while num != 0:
            count += num & 0x01
            num = num >> 1
        return count

    def countOnes3(self, num):
        count = 0
        while num != 0:
            num = num & (num - 1)
            count += 1
        return count