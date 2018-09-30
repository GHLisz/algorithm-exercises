class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


def create_tree(nums, l, r):
    if l > r: return None
    if l == r:
        n = Node(l, r)
        n.total = nums[l]
        return n
    mid = (l + r) // 2
    root = Node(l, r)
    root.left = create_tree(nums, l, mid)
    root.right = create_tree(nums, mid + 1, r)
    root.total = root.left.total + root.right.total
    return root


def update_val(root, i, val):
    if root.start == root.end:
        root.total = val
        return val
    mid = (root.start + root.end) // 2
    if i <= mid:
        update_val(root.left, i, val)
    else:
        update_val(root.right, i, val)
    root.total = root.left.total + root.right.total
    return root.total


def range_sum(root, i, j):
    if root.start == i and root.end == j:
        return root.total
    mid = (root.start + root.end) // 2
    if j <= mid:
        return range_sum(root.left, i, j)
    elif i >= mid + 1:
        return range_sum(root.right, i, j)
    else:
        return range_sum(root.left, i, mid) + range_sum(root.right, mid + 1, j)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = create_tree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        return update_val(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return range_sum(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
