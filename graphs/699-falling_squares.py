#699. Falling Squares
#Hard
#
#There are several squares being dropped onto the X-axis of a 2D plane.
#
#You are given a 2D integer array positions where positions[i] = [lefti, sideLengthi]
#represents the ith square with a side length of sideLengthi that is dropped
#with its left edge aligned with X-coordinate lefti.
#
#Each square is dropped one at a time from a height above any landed squares.
#It then falls downward until it either lands on the top side of another square
#or on the X-axis. A square brushing the left/right side of another square does
#not count as landing on it. Once it lands, it freezes in place and cannot be
#moved.
#
#After each square is dropped, you must record the height of the current tallest
#stack of squares.
#
#Return an integer array ans where ans[i] represents the height described above
#after dropping the ith square.
#
#Example 1:
#Input: positions = [[1,2],[2,3],[6,1]]
#Output: [2,5,5]
#
#Example 2:
#Input: positions = [[100,100],[200,100]]
#Output: [100,100]
#
#Constraints:
#    1 <= positions.length <= 1000
#    1 <= lefti <= 10^8
#    1 <= sideLengthi <= 10^6

class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        """
        For each new square, find max height of overlapping squares,
        then update height.
        """
        # intervals: list of (left, right, height)
        intervals = []
        result = []
        max_height = 0

        for left, side in positions:
            right = left + side
            base_height = 0

            # Find max height among overlapping intervals
            for l, r, h in intervals:
                if l < right and r > left:  # Overlap
                    base_height = max(base_height, h)

            new_height = base_height + side
            intervals.append((left, right, new_height))
            max_height = max(max_height, new_height)
            result.append(max_height)

        return result


class SolutionCoordinateCompression:
    """Use coordinate compression for efficiency"""

    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        # Coordinate compression
        coords = set()
        for left, side in positions:
            coords.add(left)
            coords.add(left + side)

        sorted_coords = sorted(coords)
        coord_map = {c: i for i, c in enumerate(sorted_coords)}

        n = len(sorted_coords)
        heights = [0] * n

        result = []
        max_height = 0

        for left, side in positions:
            right = left + side
            l_idx = coord_map[left]
            r_idx = coord_map[right]

            # Find max height in range [l_idx, r_idx)
            base_height = max(heights[l_idx:r_idx]) if l_idx < r_idx else 0
            new_height = base_height + side

            # Update heights in range
            for i in range(l_idx, r_idx):
                heights[i] = new_height

            max_height = max(max_height, new_height)
            result.append(max_height)

        return result


class SolutionSegmentTree:
    """Segment tree for range queries and updates"""

    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        # Coordinate compression
        coords = set()
        for left, side in positions:
            coords.add(left)
            coords.add(left + side)

        sorted_coords = sorted(coords)
        coord_map = {c: i for i, c in enumerate(sorted_coords)}
        n = len(sorted_coords)

        # Segment tree with lazy propagation
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push_down(node):
            if lazy[node]:
                tree[2*node] = max(tree[2*node], lazy[node])
                tree[2*node+1] = max(tree[2*node+1], lazy[node])
                lazy[2*node] = max(lazy[2*node], lazy[node])
                lazy[2*node+1] = max(lazy[2*node+1], lazy[node])
                lazy[node] = 0

        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            push_down(node)
            mid = (start + end) // 2
            return max(query(2*node, start, mid, l, r),
                       query(2*node+1, mid+1, end, l, r))

        def update(node, start, end, l, r, val):
            if r < start or end < l:
                return
            if l <= start and end <= r:
                tree[node] = max(tree[node], val)
                lazy[node] = max(lazy[node], val)
                return
            push_down(node)
            mid = (start + end) // 2
            update(2*node, start, mid, l, r, val)
            update(2*node+1, mid+1, end, l, r, val)
            tree[node] = max(tree[2*node], tree[2*node+1])

        result = []
        max_height = 0

        for left, side in positions:
            l_idx = coord_map[left]
            r_idx = coord_map[left + side] - 1

            base = query(1, 0, n-1, l_idx, r_idx)
            new_height = base + side
            update(1, 0, n-1, l_idx, r_idx, new_height)

            max_height = max(max_height, new_height)
            result.append(max_height)

        return result
