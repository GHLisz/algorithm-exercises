class Solution:
    """
    @param letters: a list of sorted characters
    @param target: a target letter
    @return: the smallest element in the list that is larger than the given target
    """

    def nextGreatestLetter(self, letters, target):
        # Write your code here
        l, h = 0, len(letters)
        while l + 1 < h:
            mid = (l + h) // 2
            if letters[mid] <= target:
                l = mid
            else:
                h = mid
        pos = l + 1 if letters[l] <= target else l

        return letters[pos]
