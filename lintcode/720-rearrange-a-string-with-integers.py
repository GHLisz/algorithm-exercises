class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """

    def rearrange(self, str):
        # Write your code here
        cs, total, num_cnt = [], 0, 0
        for c in str:
            if c.isdigit():
                total += int(c)
                num_cnt += 1
                continue
            cs.append(c)
        return ''.join(sorted(cs)) + repr(total) if num_cnt else ''.join(sorted(cs))
