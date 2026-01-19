#302. Smallest Rectangle Enclosing Black Pixels
#Hard
#
#You are given an m x n binary matrix image where 0 represents a white pixel and
#1 represents a black pixel.
#
#The black pixels are connected (i.e., there is only one black region). Pixels
#are connected horizontally and vertically.
#
#Given two integers x and y that represent the location of one of the black
#pixels, return the area of the smallest (axis-aligned) rectangle that encloses
#all black pixels.
#
#You must write an algorithm with less than O(mn) runtime complexity
#
#Example 1:
#Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
#Output: 6
#
#Example 2:
#Input: image = [["1"]], x = 0, y = 0
#Output: 1
#
#Constraints:
#    m == image.length
#    n == image[i].length
#    1 <= m, n <= 100
#    image[i][j] is either '0' or '1'.
#    1 <= x < m
#    1 <= y < n
#    image[x][y] == '1'
#    The black pixels in the image only form one component.

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # Binary search to find boundaries
        m, n = len(image), len(image[0])

        # Find leftmost column with black pixel
        def first_col_with_black(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if any(image[i][mid] == '1' for i in range(m)):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        # Find rightmost column with black pixel
        def last_col_with_black(lo, hi):
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if any(image[i][mid] == '1' for i in range(m)):
                    lo = mid
                else:
                    hi = mid - 1
            return lo

        # Find topmost row with black pixel
        def first_row_with_black(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if '1' in image[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        # Find bottommost row with black pixel
        def last_row_with_black(lo, hi):
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if '1' in image[mid]:
                    lo = mid
                else:
                    hi = mid - 1
            return lo

        left = first_col_with_black(0, y)
        right = last_col_with_black(y, n - 1)
        top = first_row_with_black(0, x)
        bottom = last_row_with_black(x, m - 1)

        return (right - left + 1) * (bottom - top + 1)

    # DFS approach O(mn) for comparison
    def minAreaDFS(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        min_row = max_row = x
        min_col = max_col = y

        def dfs(i, j):
            nonlocal min_row, max_row, min_col, max_col
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != '1':
                return
            image[i][j] = '2'  # Mark visited
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(x, y)
        return (max_row - min_row + 1) * (max_col - min_col + 1)
