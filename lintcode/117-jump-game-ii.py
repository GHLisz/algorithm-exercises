class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        step_count, last_jump_max, cur_jump_max = 0, 0, 0
        for i in range(len(A)-1):
            cur_jump_max = max(cur_jump_max, i+A[i])
            if i == last_jump_max:
                step_count += 1
                last_jump_max = cur_jump_max
        return step_count
