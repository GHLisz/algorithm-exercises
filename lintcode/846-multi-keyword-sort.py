class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """

    def multiSort(self, array):
        # Write your code here
        return sorted(array, key=lambda x: (-x[1], x[0]))
