"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if not root:
            return '{}'
        q, idx = [root], 0
        while idx < len(q):
            if q[idx]:
                q.append(q[idx].left)
                q.append(q[idx].right)
            idx += 1
        while not q[-1]:
            q.pop()

        return '{%s}' % ','.join([str(node.val) if node else '#' for node in q])

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        if data == '{}':
            return None

        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        q, idx = [root], 0
        is_left = True

        for val in vals[1:]:
            if not val == '#':
                node = TreeNode(int(val))
                if is_left:
                    q[idx].left = node
                else:
                    q[idx].right = node
                q.append(node)
            if not is_left:
                idx += 1
            is_left = not is_left
        return root
