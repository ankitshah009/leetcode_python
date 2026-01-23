#1632. Rank Transform of a Matrix
#Hard
#
#Given an m x n matrix, return a new matrix answer where answer[row][col] is
#the rank of matrix[row][col].
#
#The rank is an integer that represents how large an element is compared to
#other elements. It is calculated using the following rules:
#- The rank is an integer starting from 1.
#- If two elements p and q are in the same row or column, then:
#  - If p < q then rank(p) < rank(q)
#  - If p == q then rank(p) == rank(q)
#  - If p > q then rank(p) > rank(q)
#- The rank should be as small as possible.
#
#Example 1:
#Input: matrix = [[1,2],[3,4]]
#Output: [[1,2],[2,3]]
#Explanation: After first element 1, 2 and 3 must have ranks 2.
#After rank of 3, 4 must have rank 3.
#
#Example 2:
#Input: matrix = [[7,7],[7,7]]
#Output: [[1,1],[1,1]]
#
#Example 3:
#Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
#Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 500
#    -10^9 <= matrix[row][col] <= 10^9

from typing import List
from collections import defaultdict

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Process elements in sorted order.
        Use Union-Find to group equal elements in same row/column.
        """
        m, n = len(matrix), len(matrix[0])

        # Group positions by value
        value_to_positions = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_to_positions[matrix[i][j]].append((i, j))

        # Track maximum rank seen in each row/column
        row_max = [0] * m
        col_max = [0] * n

        result = [[0] * n for _ in range(m)]

        # Process values from smallest to largest
        for value in sorted(value_to_positions.keys()):
            positions = value_to_positions[value]

            # Union-Find for grouping equal values in same row/col
            parent = {pos: pos for pos in positions}

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[px] = py

            # Group by rows
            rows = defaultdict(list)
            cols = defaultdict(list)
            for i, j in positions:
                rows[i].append((i, j))
                cols[j].append((i, j))

            # Union positions in same row
            for pos_list in rows.values():
                for k in range(1, len(pos_list)):
                    union(pos_list[0], pos_list[k])

            # Union positions in same column
            for pos_list in cols.values():
                for k in range(1, len(pos_list)):
                    union(pos_list[0], pos_list[k])

            # Compute rank for each group
            groups = defaultdict(list)
            for pos in positions:
                groups[find(pos)].append(pos)

            for group_positions in groups.values():
                # Rank = max of (row_max, col_max) + 1 for all positions in group
                rank = 1
                for i, j in group_positions:
                    rank = max(rank, row_max[i] + 1, col_max[j] + 1)

                # Assign rank and update maximums
                for i, j in group_positions:
                    result[i][j] = rank
                    row_max[i] = rank
                    col_max[j] = rank

        return result


class SolutionSimplified:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Simplified approach with explicit Union-Find class.
        """
        m, n = len(matrix), len(matrix[0])

        class UF:
            def __init__(self):
                self.parent = {}

            def find(self, x):
                if x not in self.parent:
                    self.parent[x] = x
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                self.parent[self.find(x)] = self.find(y)

        # Sort all cells by value
        cells = sorted((matrix[i][j], i, j) for i in range(m) for j in range(n))

        result = [[0] * n for _ in range(m)]
        row_rank = [0] * m
        col_rank = [0] * n

        i = 0
        while i < len(cells):
            # Find all cells with same value
            j = i
            while j < len(cells) and cells[j][0] == cells[i][0]:
                j += 1

            # Process cells[i:j]
            uf = UF()
            val_cells = [(cells[k][1], cells[k][2]) for k in range(i, j)]

            # Union by row and column
            row_first = {}
            col_first = {}
            for r, c in val_cells:
                if r in row_first:
                    uf.union((r, c), row_first[r])
                else:
                    row_first[r] = (r, c)
                if c in col_first:
                    uf.union((r, c), col_first[c])
                else:
                    col_first[c] = (r, c)

            # Group by root
            groups = defaultdict(list)
            for r, c in val_cells:
                groups[uf.find((r, c))].append((r, c))

            # Assign ranks
            for group in groups.values():
                rank = max(max(row_rank[r], col_rank[c]) for r, c in group) + 1
                for r, c in group:
                    result[r][c] = rank
                    row_rank[r] = rank
                    col_rank[c] = rank

            i = j

        return result
