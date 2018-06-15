class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        from functools import reduce

        if not digits: return []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        func = lambda acc, digit: [x + y for x in acc for y in phone[digit]]
        return list(reduce(func, digits, ['']))
