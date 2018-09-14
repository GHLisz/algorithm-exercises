class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    def accountsMerge(self, accounts):
        # write your code here
        def sol1():  # dfs
            from collections import defaultdict

            email_to_name, graph = {}, defaultdict(set)
            for name, *emails in accounts:
                for email in emails:
                    graph[emails[0]].add(email)
                    graph[email].add(emails[0])
                    email_to_name[email] = name

            ans, seen = [], set()
            for email in graph:
                if email not in seen:
                    seen.add(email)
                    stack, component = [email], []
                    while stack:
                        node = stack.pop()
                        component.append(node)
                        for nei in graph[node]:
                            if nei not in seen:
                                seen.add(nei)
                                stack.append(nei)
                    ans.append([email_to_name[email]] + sorted(component))
            return ans

        def sol2():  # union find
            from collections import defaultdict

            class DSU:
                def __init__(self):
                    self.p = list(range(10001))

                def find(self, x):
                    if self.p[x] != x:
                        self.p[x] = self.find(self.p[x])
                    return self.p[x]

                def union(self, x, y):
                    self.p[self.find(x)] = self.find(y)

            dsu, email_to_name, email_to_id = DSU(), {}, {}

            i = 0
            for name, *emails in accounts:
                for email in emails:
                    email_to_name[email] = name
                    if email not in email_to_id:
                        email_to_id[email] = i
                        i += 1
                    dsu.union(email_to_id[emails[0]], email_to_id[email])
            ans = defaultdict(list)
            for email in email_to_name:
                ans[dsu.find(email_to_id[email])].append(email)
            return [[email_to_name[v[0]]] + sorted(v) for v in ans.values()]

        return sol2()
