class Solution:
    """
    @param: gas: An array of integers
    @param: cost: An array of integers
    @return: An integer
    """

    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if (not gas) or (not cost) or sum(gas) < sum(cost):
            return -1
        balance, position = 0, 0
        for i in range(len(gas) - 1):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                position = i + 1
        return position
