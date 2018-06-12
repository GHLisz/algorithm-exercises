"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """

    def findLeaves(self, root):
        # write your code here
        def sol1():
            def helper(root, res):
                if not root: return -1
                depth = 1 + max(helper(root.left, res), helper(root.right, res))
                if depth >= len(res):
                    res.extend([[] for _ in range(depth + 1 - len(res))])
                res[depth].append(root.val)
                return depth

            res = []
            helper(root, res)
            return res

        def sol2():
            nonlocal root

            def remove(node, leaves):
                if not node: return None
                if not node.left and not node.right:
                    leaves.append(node.val)
                    return None
                node.left = remove(node.left, leaves)
                node.right = remove(node.right, leaves)
                return node

            res = []
            while root:
                leaves = []
                root = remove(root, leaves)
                res.append(leaves)
            return res

        return sol2()
