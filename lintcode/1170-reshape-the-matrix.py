class Solution:
    """
    @param nums: List[List[int]]
    @param r: an integer
    @param c: an integer
    @return: return List[List[int]]
    """

    def matrixReshape(self, nums, r, c):
        # write your code here
        if not nums or r * c != len(nums) * len(nums[0]):
            return nums

        res = [[0] * c for _ in range(r)]
        rr, rc = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res[rr][rc] = nums[i][j]
                rc += 1
                if rc == c:
                    rr += 1
                    rc = 0
        return res
