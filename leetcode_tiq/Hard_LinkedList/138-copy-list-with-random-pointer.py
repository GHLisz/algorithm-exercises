"""
138. Copy List with Random Pointer
Medium


A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.


Note:

You must return the copy of the given head as a reference to the cloned list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # first round: make copy of each node, and link them together side-by-side in a single list.
        cur = head
        while cur:
            copy = Node(cur.val, None, None)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        # second round: assign random pointers for the copy nodes.
        cur = head
        while cur:
            cur.next.random = cur.random and cur.random.next
            cur = cur.next.next

        # third round: restore the original list, and extract the copy list.
        cur = head
        copy = head_copy = head and head.next
        while cur:
            cur.next = cur = copy.next
            copy.next = copy = cur and cur.next

        return head_copy
