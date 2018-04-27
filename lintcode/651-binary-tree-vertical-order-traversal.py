"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        from queue import Queue
        res, que = collections.defaultdict(list), Queue()
        que.put((root, 0))
        while not que.empty():
            node, x = que.get()
            if node:
                res[x].append(node.val)
                que.put((node.left, x-1))
                que.put((node.right, x+1))
        return [res[i] for i in sorted(res)]
