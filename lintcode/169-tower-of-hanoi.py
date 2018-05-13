class Solution:
    """
    @param n: the number of disks
    @return: the order of moves
    """

    def towerOfHanoi(self, n):
        # write your code here
        def play(n, from_pillar, to_pillar, aux_pillar, res):
            if n == 1:
                res.append(f'from {from_pillar} to {to_pillar}')
                return
            play(n - 1, from_pillar, aux_pillar, to_pillar, res)
            res.append(f'from {from_pillar} to {to_pillar}')
            play(n - 1, aux_pillar, to_pillar, from_pillar, res)

        res = []
        play(n, 'A', 'C', 'B', res)
        return res
