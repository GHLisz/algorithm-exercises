class Solution:
    """
    @param: n: the nth
    @return: the nth sequence
    """

    def countAndSay(self, n):
        # write your code here
        if n == 1:
            return '1'

        old_str = self.countAndSay(n - 1) + "*"
        count = 1
        new_str = ''
        for i in range(len(old_str) - 1):
            if old_str[i] == old_str[i + 1]:
                count += 1
            else:
                new_str = new_str + str(count) + old_str[i]
                count = 1
        return new_str
