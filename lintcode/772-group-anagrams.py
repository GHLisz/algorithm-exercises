class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """

    def groupAnagrams(self, strs):
        # write your code here
        import itertools
        return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]

        # hash solution
        def get_id(s):
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1
            return hash(tuple(cnt))

        m = {}
        for word in strs:
            id = get_id(word)
            group = m.get(id)
            if not group:
                group = []
                m[id] = group
            group.append(word)
        return m.values()
