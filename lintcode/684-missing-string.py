class Solution:
    """
    @param: : a given string
    @param: : another given string
    @return: An array of missing string
    """

    def missingString(self, str1, str2):
        # Write your code here
        result = []
        set2 = set(str2.split())
        for word in str1.split():
            if word not in set2:
                result.append(word)
        return result
