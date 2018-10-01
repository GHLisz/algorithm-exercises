class ConnectingGraph3:
    def __init__(self, n):
        self.component = n
        self.ids = list(range(n + 1))

    def find(self, i):
        while i != self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def connect(self, a, b):
        """
        @param a: An integer
        @param b: An integer
        @return: nothing
        """
        # write your code here
        i, j = self.find(a), self.find(b)
        if i != j:
            self.ids[i] = j
            self.component -= 1

    def query(self):
        """
        @return: An integer
        """
        # write your code here
        return self.component
