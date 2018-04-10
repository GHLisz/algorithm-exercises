class Solution:
    """
    @param str: The input string
    @return: The answer
    """

    def dataSegmentation(self, str):
        # Write your code here
        ans, ins = [], ''

        for c in str:
            if c == " ":
                if ins != "":
                    ans.append(ins)
                ins = ""
            elif c.islower():
                ins = ins + c
            else:
                if ins != "":
                    ans.append(ins)
                ans.append(c)
                ins = ""
        if ins != "":
            ans.append(ins)
        return ans
