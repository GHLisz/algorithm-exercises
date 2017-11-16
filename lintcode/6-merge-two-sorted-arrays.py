class Solution:
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        len_sum = len(A) + len(B)
        result = [0 for _ in range(len_sum)]
        A.append(999999)
        B.append(999999)
        i, j = 0, 0
        for k in range(len_sum):
            if A[i] < B[j]:
                result[k] = A[i]
                i += 1
            else:
                result[k] = B[j]
                j += 1
        return result

