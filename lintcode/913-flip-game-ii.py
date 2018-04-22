class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """

    def canWin(self, s):
        # write your code here
        def search(state):
            for i in range(len(state) - 1):
                if state[i] and state[i + 1]:
                    state[i] = state[i + 1] = False
                    if not search(state):
                        state[i] = state[i + 1] = True
                        return True
                    else:
                        state[i] = state[i + 1] = True
            return False

        state = list(map(lambda x: x == '+', s))
        return search(state)
