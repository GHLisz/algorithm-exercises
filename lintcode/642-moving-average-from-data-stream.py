class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.list = []
        self.size = size
        self.sum = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.list) >= self.size:
            self.sum -=self.list.pop(0)
        self.list.append(val)
        self.sum += val
        return self.sum / len(self.list)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
