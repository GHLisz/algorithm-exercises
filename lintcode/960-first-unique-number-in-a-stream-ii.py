class DataStream:
    def __init__(self):
        # do intialization if necessary
        self.head = ListNode(0)
        self.tail = self.head
        self.num_to_prev = {}
        self.duplicates = set()

    def add(self, num):
        """
        @param num: next number in stream
        @return: nothing
        """
        # write your code here
        if num in self.duplicates:
            return
        if num in self.num_to_prev:
            self.remove(num)
            self.duplicates.add(num)
        else:
            node = ListNode(num)
            self.num_to_prev[num] = self.tail
            self.tail.next = node
            self.tail = node

    def firstUnique(self):
        """
        @return: the first unique number in stream
        """
        # write your code here
        return self.head.next.val if self.head.next else -1

    def remove(self, num):
        prev = self.num_to_prev[num]
        prev.next = prev.next.next
        del self.num_to_prev[num]
        if prev.next is not None:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev
