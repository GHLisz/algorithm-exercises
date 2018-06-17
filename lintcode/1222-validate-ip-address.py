class Solution:
    """
    @param IP: the given IP
    @return: whether an input string is a valid IPv4 address or IPv6 address or neither
    """

    def validIPAddress(self, IP):
        # Write your code here
        def is_v4_part(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def is_v6_part(s):
            if len(s) > 4: return False
            try:
                return int(s, 16) >= 0 and s[0] != '-'
            except:
                return False

        if IP.count('.') == 3 and all(is_v4_part(s) for s in IP.split('.')): return 'IPv4'
        if IP.count(':') == 7 and all(is_v6_part(s) for s in IP.split(':')): return 'IPv6'

        return 'Neither'
