class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        ret = None
        for k in range(len(numbers)):
            l, r = k+1, len(numbers)-1
            while l<r:
                sum_ = numbers[k] + numbers[l] + numbers[r]
                if ret is None or abs(sum_ - target) < abs(ret - target):
                    ret = sum_
                if sum_ <= target:
                    l += 1
                else:
                    r -= 1
        return ret
