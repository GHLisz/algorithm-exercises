class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """

    def getStream(self, s):
        # Write your code here
        ans, cnt, dic = [], 0, [0] * 26
        for c in s:
            if dic[ord(c) - ord('a')] & 1:
                cnt -= 1
            else:
                cnt += 1
            dic[ord(c) - ord('a')] += 1
            res = 0 if cnt > 1 else 1
            ans.append(res)
        return ans
