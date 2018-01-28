class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        # Write your code here
        def helper(word, pos, cur, count, res):
            if len(word) == pos:
                res.append(cur + str(count) if count>0 else cur)
            else:
                helper(word, pos+1, cur, count+1, res)
                helper(word, pos+1, cur + (str(count) if count>0 else '') + word[pos], 0, res)
        res = []
        helper(word, 0, '', 0, res)
        return res
