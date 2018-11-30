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

        def sol1(n):  # iterative
            s = '1'
            for _ in range(n - 1):
                cur, tmp, count = s[0], '', 0
                for c in s:
                    if cur == c:
                        count += 1
                    else:
                        tmp += str(count) + cur
                        cur = c
                        count = 1
                tmp += str(count) + cur
                s = tmp
            return s

        def sol2(n):  # recursive
            if n == 1:
                return '1'

            old_str, new_str, count = sol2(n - 1) + '*', '', 1
            for i in range(len(old_str) - 1):
                if old_str[i] == old_str[i + 1]:
                    count += 1
                else:
                    new_str = new_str + str(count) + old_str[i]
                    count = 1
            return new_str

        return sol2(n)
