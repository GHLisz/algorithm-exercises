"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        # write your code here
        def merge(res, last, cur):
            if not last: return cur
            if cur.start > last.end:
                res.append(last)
                return cur
            last.end = max(last.end, cur.end)
            return last

        res, last, cur = [], None, None
        if (not list1) or (not list2):
            return res

        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                cur = list1[i]
                i += 1
            else:
                cur = list2[j]
                j += 1
            last = merge(res, last, cur)

        while i < len(list1):
            last = merge(res, last, list1[i])
            i += 1
        while j < len(list2):
            last = merge(res, last, list2[j])
            j += 1
        if last:
            res.append(last)

        return res
