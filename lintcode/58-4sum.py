class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of
              zero.
    """
    def fourSum(self ,numbers, target):
        # write your code here
        numbers.sort()
        res = []
        for i in range(len(numbers)-3):
            if i>0 and numbers[i] == numbers[i-1]:
                continue
            for j in range(i+1, len(numbers)-2):
                if j>i+1 and numbers[j] == numbers[j-1]:
                    continue
                tmp = target - numbers[i] - numbers[j]
                l, r = j+1, len(numbers)-1
                while l < r:
                    if numbers[l] + numbers[r] == tmp:
                        res.append([numbers[i], numbers[j], numbers[l], numbers[r]])
                        while l < r and numbers[l] == numbers[l+1]:
                            l += 1
                        while l < r and numbers[r] == numbers[r-1]:
                            r -= 1
                        l, r = l+1, r-1
                    elif numbers[l] + numbers[r] < tmp:
                        l += 1
                    else:
                        r -= 1
        return res
