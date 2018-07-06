class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """

    def lengthLongestPath(self, input):
        # write your code here
        max_len, path_len = 0, {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len
