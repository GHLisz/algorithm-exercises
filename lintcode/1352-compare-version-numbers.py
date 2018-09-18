class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """

    def compareVersion(self, version1, version2):
        # Write your code here
        vs1 = [int(v) for v in version1.split('.')]
        vs2 = [int(v) for v in version2.split('.')]

        for i in range(max(len(vs1), len(vs2))):
            v1 = vs1[i] if i < len(vs1) else 0
            v2 = vs2[i] if i < len(vs2) else 0
            if v1 > v2: return 1
            if v1 < v2: return -1
        return 0
