class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """

    def countArrangement(self, N):
        # Write your code here
        def sol1():
            def permute(nums, l):
                nonlocal count
                if l == len(nums): count += 1
                for i in range(l, len(nums)):
                    nums[i], nums[l] = nums[l], nums[i]
                    if nums[l] % (l + 1) == 0 or (l + 1) % nums[l] == 0:
                        permute(nums, l + 1)
                    nums[i], nums[l] = nums[l], nums[i]

            nums, count = list(range(1, N + 1)), 0
            permute(nums, 0)
            return count

        def sol2():
            def calc(n, pos, visited):
                nonlocal count
                if pos > n: count += 1
                for i in range(1, n + 1):
                    if not visited[i] and (pos % i == 0 or i % pos == 0):
                        visited[i] = True
                        calc(N, pos + 1, visited)
                        visited[i] = False

            visited, count = [False] * (N + 1), 0
            calc(N, 1, visited)
            return count

        return sol2()
