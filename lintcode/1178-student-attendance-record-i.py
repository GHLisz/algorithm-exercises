class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """

    def checkRecord(self, s):
        # Write your code here
        a = s.find('A') == -1 or s.find('A') == s.rfind('A')
        l = s.find('LLL') == -1
        return a and l
