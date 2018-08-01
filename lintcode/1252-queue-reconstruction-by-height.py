class Solution:
    """
    @param people: a random list of people
    @return: the queue that be reconstructed
    """

    def reconstructQueue(self, people):
        # write your code here
        queue = []
        for p in sorted(people, key=lambda p: (-p[0], p[1])):
            queue.insert(p[1], p)
        return queue
