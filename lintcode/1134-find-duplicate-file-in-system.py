class Solution:
    """
    @param paths: a list of string
    @return: all the groups of duplicate files in the file system in terms of their paths
    """

    def findDuplicate(self, paths):
        # Write your code here
        from collections import defaultdict

        groups = defaultdict(list)
        for path in paths:
            directory, *fcs = path.split()
            for fc in fcs:
                name, content = fc.split('(')
                groups[content].append(f'{directory}/{name}')
        return [p for p in groups.values() if len(p) > 1]
