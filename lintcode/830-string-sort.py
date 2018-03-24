class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, str):
        # Write your code here
        return "".join(char * times for char, times in
                       sorted(collections.Counter(str).most_common(),
                              key=lambda x: (-x[1], x[0])))
