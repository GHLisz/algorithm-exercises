class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """

    def validWordAbbreviation(self, word, abbr):
        # write your code here
        def sol1():
            i, j, m, n = 0, 0, len(word), len(abbr)
            while i < m and j < n:
                if '0' <= abbr[j] <= '9':
                    if abbr[j] == '0': return False
                    val = 0
                    while j < n and '0' <= abbr[j] <= '9':
                        val = val * 10 + int(abbr[j])
                        j += 1
                    i += val
                else:
                    if word[i] != abbr[j]: return False
                    i += 1
                    j += 1
            return i == m and j == n

        def sol2():
            p, cnt, m, n = 0, 0, len(word), len(abbr)

            for i in range(n):
                if '0' <= abbr[i] <= '9':
                    if cnt == 0 and abbr[i] == '0': return False
                    cnt = cnt * 10 + int(abbr[i])
                else:
                    p += cnt
                    if p >= m or word[p] != abbr[i]:
                        return False
                    p += 1
                    cnt = 0
            return p + cnt == m

        return sol1()
