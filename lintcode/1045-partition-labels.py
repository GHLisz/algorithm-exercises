class Solution:
    """
    @param S: a string
    @return: a list of integers representing the size of these parts
    """

    def partitionLabels(self, S):
        # Write your code here
        last = {c: i for i, c in enumerate(S)}
        j, anchor, ans = 0, 0, []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans
