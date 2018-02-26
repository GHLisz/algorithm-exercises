class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        source_len,  target_len = len(source), len(target)

        for i in range(0, source_len - target_len + 1):
            j = 0
            while j < target_len:
                if source[i+j] != target[j]:
                    break
                j += 1
            if j == target_len:
                return i

        return -1
