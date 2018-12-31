"""
93. Restore IP Addresses
Medium


Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def sol1():  # backtrack
            def backtrack(s, sub, ips, ip):
                if sub == 4:
                    if s == '':
                        ips.append(ip[1:])
                    return
                for i in 1, 2, 3:
                    if i <= len(s):
                        if int(s[:i]) <= 255:
                            backtrack(s[i:], sub + 1, ips, ip + '.' + s[:i])
                        if s[0] == '0':
                            break

            ips = []
            backtrack(s, 0, ips, '')
            return ips

        def sol2():  # brute force
            def is_valid(ss):
                if not ss or int(ss) > 255 or str(int(ss)) != ss:
                    return False
                return True

            res, r = [], (1, 2, 3)

            for a in r:
                for b in r:
                    for c in r:
                        for d in r:
                            if sum([a, b, c, d]) != len(s):
                                continue
                            nums_str = [s[:a], s[a:a + b], s[a + b:a + b + c], s[a + b + c:]]
                            if not all(map(is_valid, nums_str)):
                                continue
                            res.append('.'.join(nums_str))
            return res

        return sol2()
