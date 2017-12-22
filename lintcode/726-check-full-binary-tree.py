class Solution:
    """
    @param: : the given tree
    @return: Whether it is a full tree
    """

    def isFullTree(self, root):
        # write your code here
        if root is None:
            return True
        if root.left is None and root.right is not None:
            return False
        if root.left is not None and root.right is None:
            return False

        return self.isFullTree(root.left) and self.isFullTree(root.right)
