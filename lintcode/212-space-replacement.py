class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if string is None:
            return length

        spaces = 0
        for c in string:
            if c == ' ':
                spaces += 1
        L = length + spaces * 2
        ptr = L - 1

        for i in range(length - 1, -1, -1):
            if string[i] == ' ':
                string[ptr] = '0'
                string[ptr - 1] = '2'
                string[ptr - 2] = '%'
                ptr -= 3
            else:
                string[ptr] = string[i]
                ptr -= 1

        return L
