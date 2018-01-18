class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
