class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        from collections import defaultdict

        m = defaultdict(list)
        for w in strs:
            m[''.join(sorted(w))].append(w)

        return [s for v in m.values() if len(v) > 1 for s in v]
