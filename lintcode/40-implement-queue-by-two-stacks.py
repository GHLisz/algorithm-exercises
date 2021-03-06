class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        self.adjust()
        return self.stack2.pop()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        self.adjust()
        return self.stack2[-1]

