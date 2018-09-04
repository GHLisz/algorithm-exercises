class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        r = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                r.append("fizz buzz")
            elif i % 3 == 0:
                r.append('fizz')
            elif i % 5 == 0:
                r.append('buzz')
            else:
                r.append(str(i))
        return r
