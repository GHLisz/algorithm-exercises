"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        def quicksort(nuts, bolts, low, high, compare):
            if low < high:
                idx = partition(nuts, low, high, bolts[high], compare)  # get the pivot nuts's idx
                partition(bolts, low, high, nuts[idx], compare)  # the positions get aligned
                quicksort(nuts, bolts, low, idx - 1, compare)
                quicksort(nuts, bolts, idx + 1, high, compare)

        def partition(arr, low, high, pivot, compare):
            i, j = low - 1, low
            while j < high:
                state1 = compare.cmp(arr[j], pivot)
                state2 = compare.cmp(pivot, arr[j])
                if state1 == -1 or state2 == 1:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 1
                elif state1 == 0 or state2 == 0:
                    arr[j], arr[high] = arr[high], arr[j]
                else:
                    j += 1
            i += 1
            arr[i], arr[high] = arr[high], arr[i]
            return i

        if not all([nuts, bolts, compare]):
            return
        if len(nuts) != len(bolts):
            return

        quicksort(nuts, bolts, 0, len(nuts) - 1, compare)
