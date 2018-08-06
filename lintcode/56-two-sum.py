class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        m = {}
        for i, v in enumerate(numbers):
            if target - v in m: return [m[target - v], i]
            m[v] = i
        return [None, None]
