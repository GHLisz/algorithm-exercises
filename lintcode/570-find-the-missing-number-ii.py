class Solution:
    """
    @param: n: An integer
    @param: str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        # write your code here
        def find(n, str, index, used):
            if index == len(str):
                results = []
                for i in range(1, n + 1):
                    if not used[i]:
                        results.append(i)
                return results[0] if len(results) == 1 else -1

            if str[index] == '0':
                return -1

            for i in range(1, 3):
                num = int(str[index:index + i])
                if 1 <= num <= n and not used[num]:
                    used[num] = True
                    target = find(n, str, index + i, used)
                    if target != -1:
                        return target
                    used[num] = False
            return -1

        used = [False] * (n + 1)
        return find(n, str, 0, used)
