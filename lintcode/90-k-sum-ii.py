class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        # write your code here
        def dfs(A, k, target, index, tmp, res):
            if target == 0 and k == 0:
                res.append(tmp[:])
                return
            if len(A) == index or target < 0 or k < 0:
                return
            dfs(A, k, target, index+1, tmp, res)
            tmp.append(A[index])
            dfs(A, k-1, target-A[index], index+1, tmp, res)
            tmp.pop()

        res = []
        dfs(A, k, target, 0, [], res)
        return res
