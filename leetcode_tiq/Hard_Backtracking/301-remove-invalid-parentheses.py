"""
301. Remove Invalid Parentheses
Hard


Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        valid_expressions = set()
        min_removed = float('inf')

        def remaining(string, index, left_count, right_count, expr, rem_count):
            nonlocal valid_expressions, min_removed

            if index == len(string):
                if left_count == right_count:
                    if rem_count <= min_removed:
                        possible_ans = ''.join(expr)
                        if rem_count < min_removed:
                            valid_expressions = set()
                            min_removed = rem_count
                        valid_expressions.add(possible_ans)
                return

            current_char = string[index]

            if current_char not in ['(', ')']:
                expr.append(current_char)
                remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
                return

            remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)

            expr.append(current_char)
            if string[index] == '(':
                remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)
            elif right_count < left_count:
                remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)
            expr.pop()

        remaining(s, 0, 0, 0, [], 0)
        return list(valid_expressions)
