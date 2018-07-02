class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end: return 1
        front, back, dic, dist = {start}, {end}, set(dict), 2
        dic.discard(start)

        while front:
            # generate all valid transformations
            front = dic & (set(word[:index] + ch + word[index + 1:]
                               for word in front
                               for index in range(len(word))
                               for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return dist
            dist += 1
            if len(front) > len(back):
                # swap front and back for better performance
                # (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from dic to avoid cycle
            dic -= front
        return 0
