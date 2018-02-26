class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        # Write your code here
        index = 1
        factor = 1
        for i in range(len(A)-1, -1, -1):
            smaller_num_count = 0
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    smaller_num_count += 1
            index += factor * smaller_num_count
            factor *= len(A) - i
        return index
