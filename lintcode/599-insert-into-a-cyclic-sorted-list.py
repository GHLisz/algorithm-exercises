"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """

    def insert(self, node, x):
        # write your code here
        if not node:
            new_node = ListNode(x)
            new_node.next = new_node
            return new_node

        cur, pre = node, None
        while True:
            pre, cur = cur, cur.next
            if pre.val <= x <= cur.val:
                break
            if pre.val > cur.val and (x < cur.val or x > pre.val):
                break
            if cur is node:
                break

        new_node = ListNode(x)
        new_node.next = cur
        pre.next = new_node
        return new_node
