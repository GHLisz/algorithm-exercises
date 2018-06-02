class Solution:
    """
    @param N: a positive number
    @return: how many numbers X from 1 to N are good
    """

    def rotatedDigits(self, N):
        # write your code here
        def is_valid(num):
            d = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
            num_str = str(num)
            rotated_num_str = ''
            for digit_str in num_str:
                if digit_str in d:
                    rotated_num_str += d[digit_str]
            if len(num_str) != len(rotated_num_str) or num_str == rotated_num_str:
                return False
            return True

        res = 0
        for n in range(1, N + 1):
            res += 1 if is_valid(n) else 0
        return res
