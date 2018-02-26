class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        # write your code here
        max_len, ans = 0, []
        for w in dictionary:
            if len(w) > max_len:
                max_len = len(w)
                del ans[:]
                ans.append(w)
            elif len(w) == max_len:
                ans.append(w)
        return ans
