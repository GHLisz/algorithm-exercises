"""
118. Pascal's Triangle
Easy


Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px"><br>
<small>In Pascal's triangle, each number is the sum of the two numbers directly above it.</small></p>

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for _ in range(numRows - 1):
            res.append([x + y for x, y in
                        zip(res[-1] + [0], [0] + res[-1])])

        return res[:numRows]
