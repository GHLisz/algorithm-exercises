class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order
    """
    def reverseStore(self, head):
        # write your code here
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.reverse()
        return res
