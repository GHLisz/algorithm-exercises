"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: ListNode head is the head of the linked list
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(1, m):
            cur = cur.next

        pre_m_node = cur
        m_node = cur.next
        n_node = m_node
        post_n_node = m_node.next

        for i in range(m, n):
            temp = post_n_node.next
            post_n_node.next = n_node
            n_node = post_n_node
            post_n_node = temp

        m_node.next = post_n_node
        pre_m_node.next = n_node

        return dummy.next
