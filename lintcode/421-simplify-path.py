class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """

    def simplifyPath(self, path):
        # write your code here
        places, stack = [p for p in path.split('/') if p and p != '.'], []
        for p in places:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
