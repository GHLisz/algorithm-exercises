class Solution:
    """
    @param preorder: a string
    @return: return a bool
    """

    def isValidSerialization(self, preorder):
        # write your code here
        def sol1():
            nodes = preorder.split(',')
            diff = 1  # diff = outdegree - indegree
            for node in nodes:
                diff -= 1
                if diff < 0: return False
                if node != '#': diff += 2
            return diff == 0

        def sol2():
            if not preorder: return False

            st, nodes = [], preorder.split(',')

            for pos, cur in enumerate(nodes):
                while cur == '#' and st and st[-1] == cur:
                    st.pop()
                    if not st: return False
                    st.pop()
                st.append(cur)

            return len(st) == 1 and st[-1] == '#'

        return sol2()
