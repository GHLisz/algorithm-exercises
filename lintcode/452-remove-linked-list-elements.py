# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if head is None:
            return head

        cur_node, next_node = head, head.next
        while next_node is not None:
            if next_node.val == val:
                cur_node.next = next_node.next
                next_node = next_node.next
            else:
                cur_node, next_node = cur_node.next, next_node.next

        if head.val == val:
            head = head.next

        return head
