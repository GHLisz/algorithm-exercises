"""
207. Course Schedule
Medium


There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def sol1():  # bfs
            graph, degree, queue, count = [[] for _ in range(numCourses)], [0] * numCourses, [], 0

            for p0, p1 in prerequisites:
                degree[p1] += 1
                graph[p0].append(p1)

            for i, d in [(i, d) for i, d in enumerate(degree) if d == 0]:
                queue.append(i)
                count += 1

            while queue:
                course = queue.pop(0)
                for i in range(len(graph[course])):
                    pointer = graph[course][i]
                    degree[pointer] -= 1
                    if degree[pointer] == 0:
                        queue.append(pointer)
                        count += 1

            return count == numCourses

        def sol2():  # dfs
            def dfs(graph, visited, course):
                if visited[course]:
                    return False
                else:
                    visited[course] = True

                for i in range(len(graph[course])):
                    if not dfs(graph, visited, graph[course][i]):
                        return False

                visited[course] = False
                return True

            graph, visited = [[] for _ in range(numCourses)], [False] * numCourses

            for p0, p1 in prerequisites:
                graph[p1].append(p0)

            for i in range(numCourses):
                if not dfs(graph, visited, i):
                    return False

            return True

        return sol2()
