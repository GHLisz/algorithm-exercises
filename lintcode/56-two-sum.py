class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target-numbers[i]] + 1, i+1]
            hash[numbers[i]] = i
        return [None, None]
