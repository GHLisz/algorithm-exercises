"""
347. Top K Frequent Elements
Medium


Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sol1():  # bucket sort
            bucket, freq_map = [[] for _ in range(len(nums) + 1)], {}

            for n in nums:
                freq_map[n] = freq_map.get(n, 0) + 1

            for key in freq_map.keys():
                freq = freq_map[key]
                bucket[freq].append(key)

            res = []

            pos = len(nums)
            while pos >= 0 and len(res) < k:
                if bucket[pos]:
                    res.extend(bucket[pos])
                pos -= 1
            return res[:k]

        def sol2():  # max heap
            import heapq, collections
            c = collections.Counter(nums)
            h = [(-freq, num) for num, freq in c.items()]
            heapq.heapify(h)
            return [heapq.heappop(h)[1] for _ in range(k)]

        return sol1()
