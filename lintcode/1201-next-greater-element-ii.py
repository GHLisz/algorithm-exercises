class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """

    def nextGreaterElements(self, nums):
        # Write your code here
        n = len(nums)
        res = [0] * n
        st = []
        for i in range(2 * n - 1, -1, -1):
            while len(st) and nums[st[-1]] <= nums[i % n]:
                st.pop()
            res[i % n] = nums[st[-1]] if len(st) else -1
            st.append(i % n)
        return res
