class Solution:
    """
    @param s: a string
    @return: the number of substrings
    """
    def countBinarySubstrings(self, s):
        # Write your code here
        # First, I count the number of 1 or 0 grouped consecutively.
        # For example "0110001111" will be [1, 2, 3, 4].
        g = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        g = list(g)
        # Second, for any possible substrings with 1 and 0 grouped consecutively,
        # the number of valid substring will be the minimum number of 0 and 1.
        # For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")
        return sum(min(a, b) for a, b in zip(g, g[1:]))
