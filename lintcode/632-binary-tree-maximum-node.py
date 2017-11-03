class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        # Write your code here
        if root is None:
            return root

        max_node = root

        if root.left is not None:
            left = self.maxNode(root.left)
            max_node = max_node if max_node.val > left.val else left

        if root.right is not None:
            right = self.maxNode(root.right)
            max_node = max_node if max_node.val > right.val else right

        return max_node
