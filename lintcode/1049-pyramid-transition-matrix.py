class Solution:
    """
    @param bottom: a string
    @param allowed: a list of strings
    @return: return a boolean
    """

    def pyramidTransition(self, bottom, allowed):
        # write your code here
        from collections import defaultdict

        T = defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        seen = set()

        def solve(A):
            if len(A) == 1: return True
            if A in seen: return False
            seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i=0):
            if i + 1 == len(A):
                yield ''.join(ans)
            else:
                for w in T[A[i], A[i + 1]]:
                    ans.append(w)
                    for result in build(A, ans, i + 1):
                        yield result
                    ans.pop()

        return solve(bottom)
