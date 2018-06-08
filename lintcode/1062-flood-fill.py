class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """

    def floodFill(self, image, sr, sc, newColor):
        # Write your code here
        rows, cols, old_color = len(image), len(image[0]), image[sr][sc]

        def t(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != old_color:
                return
            image[row][col] = newColor
            for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                t(row + x, col + y)

        if old_color != newColor:
            t(sr, sc)

        return image
