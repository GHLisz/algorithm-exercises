"""
601. Flatten 2D Vector


Implement an iterator to flatten a 2d vector.

Example
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
"""


class Vector2D(object):
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row, self.col, self.v = 0, 0, vec2d

    # @return {int} a next element
    def next(self):
        # Write your code here
        if not self.hasNext():
            raise StopIteration

        self.col += 1
        return self.v[self.row][self.col - 1]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.row < len(self.v) and self.col >= len(self.v[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.v)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
