class Solution:
    """
    @param answers: some subset of rabbits (possibly all of them) tell
    @return: the minimum number of rabbits that could be in the forest.
    """

    def numRabbits(self, answers):
        # write your code here
        import collections, math
        c = collections.Counter(answers)
        # If x+1 rabbits have same color, then we get x+1 rabbits who all answer x.
        return sum(math.ceil(c[x] / (x + 1)) * (x + 1) for x in c)
