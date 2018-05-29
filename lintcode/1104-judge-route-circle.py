class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        from collections import Counter
        c = Counter(moves)
        return c['U'] == c['D'] and c['L'] == c['R']
