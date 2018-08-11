class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def originalDigits(self, s):
        # write  your code here
        cnt = [0] * 10
        for c in s:
            if c == 'z': cnt[0] += 1
            if c == 'w': cnt[2] += 1
            if c == 'x': cnt[6] += 1
            if c == 's': cnt[7] += 1  # 7-6
            if c == 'g': cnt[8] += 1
            if c == 'u': cnt[4] += 1
            if c == 'f': cnt[5] += 1  # 5-4
            if c == 'h': cnt[3] += 1  # 3-8
            if c == 'i': cnt[9] += 1  # 9-8-5-6
            if c == 'o': cnt[1] += 1  # 1-0-2-4
        cnt[7] -= cnt[6]
        cnt[5] -= cnt[4]
        cnt[3] -= cnt[8]
        cnt[9] = cnt[9] - cnt[8] - cnt[5] - cnt[6]
        cnt[1] = cnt[1] - cnt[0] - cnt[2] - cnt[4]
        return ''.join(str(i) for i in range(10) for _ in range(cnt[i]))
