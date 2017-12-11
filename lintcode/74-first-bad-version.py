"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
bad version.
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        l, h = 1, n
        while l + 1 < h:
            m = (l+h) // 2
            if SVNRepo.isBadVersion(m):
                h = m
            else:
                l = m
        return l if SVNRepo.isBadVersion(l) else h
