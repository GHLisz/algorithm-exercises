class StringUtils:
    """
    @param: originalStr: the string we want to append to
    @param: size: the target length of the string
    @param: padChar: the character to pad to the left side of the string
    @return: A string
    """
    def leftPad(self, originalStr, size, padChar=' '):
        # write your code here
        return padChar * (size - len(originalStr)) + originalStr
