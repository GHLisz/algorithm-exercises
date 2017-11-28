class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        res = []
        numbers.sort()
        for k in range(len(numbers)):
            if numbers[k] > 0:
                break
            if k > 0 and numbers[k] == numbers[k - 1]:
                continue
            target = 0 - numbers[k]
            i, j = k + 1, len(numbers) - 1
            while i < j:
                if numbers[i] + numbers[j] == target:
                    res.append([numbers[k], numbers[i], numbers[j]])
                    while i < j and numbers[i] == numbers[i + 1]:
                        i += 1
                    while i < j and numbers[j] == numbers[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif numbers[i] + numbers[j] < target:
                    i += 1
                else:
                    j -= 1
        return res
