class Solution:
    """
    @param a: a string
    @param b: a string
    @return: a string representing their multiplication
    """

    def complexNumberMultiply(self, a, b):
        # Write your code here
        ar, ai = map(int, a[:-1].split('+'))
        br, bi = map(int, b[:-1].split('+'))
        return f'{ar*br-ai*bi}+{ar*bi+ai*br}i'
