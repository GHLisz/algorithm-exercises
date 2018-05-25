class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        def dfs(s, sub, ips, ip):
            if sub == 4:
                if s == '':
                    ips.append(ip[1:])
                return
            for i in range(1, 4):    # the three ifs' order cannot be changed!
                if i <= len(s):      # if i > len(s), s[:i] will make false!!!!
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
                    if s[0] == '0': break
        ips = []
        dfs(s, 0, ips, '')
        return ips
