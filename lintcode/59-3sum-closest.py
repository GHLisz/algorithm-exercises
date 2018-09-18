class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        res, numbers = None, sorted(numbers)

        for k in range(len(numbers)):
            l, r = k + 1, len(numbers) - 1

            while l < r:
                total = numbers[k] + numbers[l] + numbers[r]

                if res is None or abs(total - target) < abs(res - target):
                    res = total

                if total <= target:
                    l += 1
                else:
                    r -= 1
        return res
