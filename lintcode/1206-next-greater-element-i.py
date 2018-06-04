class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """

    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        d, st = {}, []
        # d: map from x to next greater elem of x

        for num in nums2:
            while len(st) and st[-1] < num:
                d[st.pop()] = num
            st.append(num)

        return [d.get(num, -1) for num in nums1]
