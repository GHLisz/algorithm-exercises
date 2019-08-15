"""
547. Friend Circles
Medium


There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def sol1():  # dfs
            cnt, visited, n = 0, [0] * len(M), len(M)

            def dfs(i):
                for j in range(n):
                    if not visited[j] and M[i][j]:
                        visited[j] = 1
                        dfs(j)

            for i in range(n):
                if not visited[i]:
                    cnt += 1
                    dfs(i)

            return cnt

        def sol2():
            n = len(M)
            res, p = [n], {i: i for i in range(n)}

            def find(x):
                while x != p[x]:
                    p[x] = p[p[x]]
                    x = p[x]
                return p[x]

            def union(x, y):
                rx, ry = find(x), find(y)
                if rx != ry:
                    res[0] -= 1
                    p[rx] = ry

            for i in range(n):
                for j in range(i + 1, n):
                    if M[i][j]:
                        union(i, j)
            return res[0]

        return sol2()
