class Solution:
    """
    @param senate: a string
    @return: return a string
    """

    def predictPartyVictory(self, senate):
        # write your code here
        from collections import deque

        queue, people, bans = deque(), [0, 0], [0, 0]

        for person in senate:
            x = person == 'R'
            people[x] += 1
            queue.append(x)

        while all(people):
            x = queue.popleft()
            if bans[x]:
                bans[x] -= 1
                people[x] -= 1
            else:
                bans[not x] += 1
                queue.append(x)

        return "Radiant" if people[1] else "Dire"
