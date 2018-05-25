class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """

    def countOfSmallerNumber(self, A, queries):
        # write your code here
        def sol1():  # binary search
            def binary(A, q):
                if len(A) == 0 or A[-1] < q:
                    return len(A)

                start, end = 0, len(A) - 1
                while start + 1 < end:
                    mid = (start + end) // 2
                    if A[mid] < q:
                        start = mid
                    else:
                        end = mid
                if A[start] >= q: return start
                if A[end] >= q: return end
                return end + 1

            L = sorted(A)
            return [binary(L, q) for q in queries]

        def sol2():
            class Node:
                def __init__(self, start, end, count):
                    self.start = start
                    self.end = end
                    self.count = count
                    self.left = None
                    self.right = None

            def build(start, end):
                if start >= end:
                    return Node(start, end, 0)
                root = Node(start, end, 0)
                mid = (start + end) // 2
                root.left = build(start, mid)
                root.right = build(mid + 1, end)
                return root

            def modify(root, index, value):
                if root.start == index == root.end:
                    root.count += value
                    return
                mid = (root.start + root.end) // 2
                if index <= mid:
                    modify(root.left, index, value)
                if index > mid:
                    modify(root.right, index, value)
                root.count = root.left.count + root.right.count

            def query(root, start, end):
                if start == root.start and end == root.end:
                    return root.count
                mid = (root.start + root.end) // 2
                if end <= mid:
                    return query(root.left, start, end)
                if start > mid:
                    return query(root.right, start, end)
                return query(root.left, start, mid) \
                       + query(root.right, mid + 1, end)

            root, res = build(0, 10000), []
            for num in A:
                modify(root, num, 1)
            for q in queries:
                count = query(root, 0, q - 1) if q > 0 else 0
                res.append(count)
            return res

        return sol2()
