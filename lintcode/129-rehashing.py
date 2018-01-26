"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        # write your code here
        def add_node(hash_table, number):
            c = number % len(hash_table)
            if hash_table[c] is None:
                hash_table[c] = ListNode(number)
            else:
                add_listnode(hash_table[c], number)

        def add_listnode(node, number):
            if node.next is not None:
                add_listnode(node.next, number)
            else:
                node.next = ListNode(number)

        res = [None for _ in range(2 * len(hashTable))]
        for item in hashTable:
            p = item
            while p is not None:
                add_node(res, p.val)
                p = p.next
        return res
