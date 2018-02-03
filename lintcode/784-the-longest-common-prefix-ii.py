class Solution:
    """
    @param dic: the n strings
    @param target: the target string
    @return: The ans
    """
    def theLongestCommonPrefix(self, dic, target):
        # write your code here
        def prefix_len(str1, str2=target):
            cnt = 0
            for i in range(min(len(str1), len(str2))):
                if str1[i] == str2[i]:
                    cnt += 1
                else:
                    break
            return cnt
        return max(map(prefix_len, dic))
