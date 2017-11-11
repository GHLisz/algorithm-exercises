"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            r = Guess.guess(mid)
            if r < 0:
                high = mid - 1
            if r == 0:
                return mid
            if r > 0:
                low = mid + 1
        return -1
