"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """

    def widthOfBinaryTree(self, root):
        # Write your code here
        def sol1():  # bfs
            queue = [(root, 0, 0)]
            cur_depth = left = res = 0
            for node, depth, pos in queue:
                if not node: continue
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                res = max(pos - left + 1, res)
            return res

        def sol2():  # dfs
            res, left = 0, {}

            def dfs(node, depth=0, pos=0):
                nonlocal res
                if not node: return
                left.setdefault(depth, pos)
                res = max(res, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

            dfs(root)
            return res

        return sol1()
