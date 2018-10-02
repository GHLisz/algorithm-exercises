class ZigzagIterator:

    def __init__(self, v1, v2):
        """
        @param: v1: A 1d vector
        @param: v2: A 1d vector
        """
        # do intialization if necessary
        self.queue = list(filter(bool, [v1, v2]))

    def next(self):
        """
        @return: An integer
        """
        # write your code here
        v = self.queue.pop(0)
        ret = v.pop(0)
        if v: self.queue.append(v)
        return ret

    def hasNext(self):
        """
        @return: True if has next
        """
        # write your code here
        return bool(self.queue)

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result
