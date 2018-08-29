class Solution:
    """
    @param asteroids: a list of integers
    @return: return a list of integers
    """

    def asteroidCollision(self, asteroids):
        # write your code here
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans
