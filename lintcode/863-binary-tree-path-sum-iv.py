class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """

    def pathSum(self, nums):
        # write your code here
        def sol1():
            class Node:
                def __init__(self, val):
                    self.val, self.left, self.right = val, None, None

            root = Node(nums[0] % 10)
            for x in nums[1:]:
                depth, pos, val = x // 100, x // 10 % 10, x % 10
                pos -= 1
                cur = root
                for d in range(depth - 2, -1, -1):
                    if pos < 2 ** d:
                        cur.left = cur = cur.left or Node(val)
                    else:
                        cur.right = cur = cur.right or Node(val)
                    pos %= 2 ** d

            ans = 0

            def dfs(root, cur_sum):
                nonlocal ans
                if not root: return
                cur_sum += root.val
                if not root.left and not root.right:
                    ans += cur_sum
                else:
                    dfs(root.left, cur_sum)
                    dfs(root.right, cur_sum)

            dfs(root, 0)
            return ans

        def sol2():
            ans, values = 0, {x // 10: x % 10 for x in nums}

            def dfs(node, cur_sum):
                nonlocal ans
                if node not in values: return
                cur_sum += values[node]
                depth, pos = divmod(node, 10)
                left = (depth + 1) * 10 + 2 * pos - 1
                right = left + 1

                if left not in values and right not in values:
                    ans += cur_sum
                else:
                    dfs(left, cur_sum)
                    dfs(right, cur_sum)

            dfs(nums[0] // 10, 0)
            return ans

        return sol2()
