"""
38. Count and Say
Easy


The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def sol1(n):  # recursive
            if n == 1:
                return '1'

            old, new, count = sol1(n - 1) + '*', '', 1
            for i in range(len(old) - 1):
                if old[i] != old[i + 1]:
                    new += str(count) + old[i]
                    count = 1
                else:
                    count += 1

            return new

        def sol2(n):  # iterative
            old = '1'
            for _ in range(n - 1):
                cur, new, count = old[0], '', 0
                for c in old:
                    if cur == c:
                        count += 1
                    else:
                        new += str(count) + cur
                        cur = c
                        count = 1
                new += str(count) + cur
                old = new
            return old

        return sol2(n)
