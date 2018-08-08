class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """

    def increasingTriplet(self, nums):
        # write your code
        def sol1():  # generalized
            import bisect
            k = 3
            inc = [float('inf')] * (k - 1)
            for n in nums:
                i = bisect.bisect_left(inc, n)
                if i >= k - 1:
                    return True
                inc[i] = n
            return k == 0

        def sol2():
            # candidates for 1st & 2nd elements
            c1 = c2 = float('inf')
            for n in nums:
                if n <= c1:
                    c1 = n
                elif n <= c2:
                    c2 = n
                else:
                    return True
            return False

        return sol1()
