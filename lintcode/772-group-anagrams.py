class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """

    def groupAnagrams(self, strs):
        # write your code here
        def sol1():
            import itertools
            return [sorted(g) for _, g in itertools.groupby(
                sorted(strs, key=sorted), sorted)]

        def sol2():
            import collections
            ans = collections.defaultdict(list)
            for s in strs:
                count = [0] * 26
                for c in s:
                    count[ord(c) - ord('a')] += 1
                ans[tuple(count)].append(s)
            return ans.values()

        return sol2()
