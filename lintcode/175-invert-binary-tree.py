"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root):
        # write your code here
        def recursive(root):
            if not root: return
            root.left, root.right = root.right, root.left
            list(map(recursive, [root.left, root.right]))

        def iterative(root):
            if not root: return None
            que = [root]
            while que:
                cur = que.pop(0)
                cur.left, cur.right = cur.right, cur.left
                for sub in cur.left, cur.right:
                    if sub:
                        que.append(sub)
            return root

        return iterative(root)
