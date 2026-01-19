#733. Flood Fill
#Easy
#
#An image is represented by an m x n integer grid image where image[i][j] represents the pixel
#value of the image.
#
#You are also given three integers sr, sc, and color. You should perform a flood fill on the
#image starting from the pixel image[sr][sc].
#
#To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
#to the starting pixel of the same color as the starting pixel, plus any pixels connected
#4-directionally to those pixels (also with the same color), and so on. Replace the color of
#all of the aforementioned pixels with color.
#
#Return the modified image after performing the flood fill.
#
#Example 1:
#Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]
#
#Example 2:
#Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
#Output: [[0,0,0],[0,0,0]]
#
#Constraints:
#    m == image.length
#    n == image[i].length
#    1 <= m, n <= 50
#    0 <= image[i][j], color < 2^16
#    0 <= sr < m
#    0 <= sc < n

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if image[r][c] != original_color:
                return

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
