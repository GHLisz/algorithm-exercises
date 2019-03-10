"""
42. Trapping Rain Water
Hard


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        def sol1():  # two pointers
            l, r, water, plank = 0, len(height) - 1, 0, 0
            while l < r:
                while l < r and height[l] <= plank:
                    water += plank - height[l]
                    l += 1
                while l < r and height[r] <= plank:
                    water += plank - height[r]
                    r -= 1
                plank = min(height[l], height[r])
            return water

        def sol2():  # stack
            s, i, n, res = [], 0, len(height), 0
            while i < n:
                if not s or height[i] <= height[s[-1]]:
                    s.append(i)
                    i += 1
                else:
                    t = s.pop()
                    if not s:
                        continue
                    res += (min(height[i], height[s[-1]]) - height[t]) * (i - s[-1] - 1)
            return res

        return sol1()
