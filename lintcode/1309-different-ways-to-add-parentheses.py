class Solution:
    """
    @param input: a string
    @return: return List[int]
    """

    def diffWaysToCompute(self, input):
        # write your code here
        return [eval(`a` + c + `b`)
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]
