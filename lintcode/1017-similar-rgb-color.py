class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """

    def similarRGB(self, color):
        # Write your code here
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        a = '00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff'.split()
        p = [(a[i], a[j], a[k]) for i in range(16) for j in range(16) for k in range(16)]
        res, mn = '', 999999
        for s in p:
            zs = zip(s, (r, g, b))
            d = sum((int(z[0], 16) - z[1]) ** 2 for z in zs)
            if mn > d:
                mn = d
                res = s
        return '#' + ''.join(res)
