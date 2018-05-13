"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        # write your code here
        def sol1():
            def tobst(head, tail):
                if head == tail:
                    return None
                slow, fast = head, head
                while fast != tail and fast.next != tail:
                    slow = slow.next
                    fast = fast.next.next
                root = TreeNode(slow.val)
                root.left = tobst(head, slow)
                root.right = tobst(slow.next, tail)
                return root

            if not head: return None
            return tobst(head, None)

        def sol2():
            def build(low, high):
                nonlocal current
                if low >= high:
                    return None
                tmp = TreeNode(None)
                mid = (low + high) // 2
                tmp.left = build(low, mid)
                tmp.val = current.val
                current = current.next
                tmp.right = build(mid + 1, high)
                return tmp

            nonlocal head
            current = head
            len_ = 0
            while head:
                len_ += 1
                head = head.next
            return build(0, len_)

        return sol2()
