class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        array = list(range(129))
        for i in range(129):
            array[i] = 0
        for i in range(len(str)):
            if array[ord(str[i])] == 0:
                array[ord(str[i])] = 1
            else:
                return False
        return True
