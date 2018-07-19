class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.capacity = n
        self.arr = [0] * n
        self.head = 0
        self.tail = -1

    """
    @return:  return true if the array is full
    """

    def isFull(self):
        # write your code here
        return self.tail - self.head + 1 == self.capacity

    """
    @return: return true if there is no element in the array
    """

    def isEmpty(self):
        # write your code here
        return self.tail < self.head

    """
    @param element: the element given to be added
    @return: nothing
    """

    def enqueue(self, element):
        # write your code here
        self.tail += 1
        if self.tail + 1 < self.capacity:
            self.arr[self.tail] = element
        else:
            self.arr[self.tail % self.capacity] = element

    """
    @return: pop an element from the queue
    """

    def dequeue(self):
        # write your code here
        idx = self.head if self.head < self.capacity else self.head % self.capacity
        self.head += 1
        return self.arr[idx]
