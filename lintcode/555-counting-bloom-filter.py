class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do initialization if necessary
        self.k = k
        self.hash_func = [HashFunction(100000 + i, 2 * i + 3) for i in range(k)]
        self.bits = [0] * (100000 + k)

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        for i in range(self.k):
            pos = self.hash_func[i].hash(word)
            self.bits[pos] += 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        # write your code here
        for i in range(self.k):
            pos = self.hash_func[i].hash(word)
            self.bits[pos] -= 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        # write your code here
        for i in range(self.k):
            pos = self.hash_func[i].hash(word)
            if self.bits[pos] <= 0:
                return False
        return True


class HashFunction:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, values):
        ret = 0
        for v in values:
            ret += self.seed * ret + ord(v)
            ret %= self.cap
        return ret
