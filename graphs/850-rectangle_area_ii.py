#850. Rectangle Area II
#Hard
#
#You are given a 2D array of axis-aligned rectangles. Each rectangle[i] =
#[xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the
#coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates
#of the top-right corner.
#
#Calculate the total area covered by all rectangles in the plane. Any area
#covered by two or more rectangles should only be counted once.
#
#Return the total area. Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
#Output: 6
#
#Example 2:
#Input: rectangles = [[0,0,1000000000,1000000000]]
#Output: 49 (due to modulo)
#
#Constraints:
#    1 <= rectangles.length <= 200
#    rectangles[i].length == 4
#    0 <= xi1, yi1, xi2, yi2 <= 10^9
#    xi1 <= xi2
#    yi1 <= yi2

class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        """
        Coordinate compression + sweep line algorithm.
        """
        MOD = 10**9 + 7

        # Collect all x and y coordinates
        x_coords = set()
        y_coords = set()

        for x1, y1, x2, y2 in rectangles:
            x_coords.add(x1)
            x_coords.add(x2)
            y_coords.add(y1)
            y_coords.add(y2)

        x_sorted = sorted(x_coords)
        y_sorted = sorted(y_coords)

        x_idx = {x: i for i, x in enumerate(x_sorted)}
        y_idx = {y: i for i, y in enumerate(y_sorted)}

        # Mark cells covered by rectangles
        covered = [[False] * len(y_sorted) for _ in range(len(x_sorted))]

        for x1, y1, x2, y2 in rectangles:
            for i in range(x_idx[x1], x_idx[x2]):
                for j in range(y_idx[y1], y_idx[y2]):
                    covered[i][j] = True

        # Calculate total area
        total = 0
        for i in range(len(x_sorted) - 1):
            for j in range(len(y_sorted) - 1):
                if covered[i][j]:
                    width = x_sorted[i + 1] - x_sorted[i]
                    height = y_sorted[j + 1] - y_sorted[j]
                    total += width * height

        return total % MOD


class SolutionSweepLine:
    """Sweep line with segment tree (conceptual)"""

    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 10**9 + 7

        # Create events: (x, type, y1, y2) where type: 0=start, 1=end
        events = []
        y_coords = set()

        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 0, y1, y2))  # Start
            events.append((x2, 1, y1, y2))  # End
            y_coords.add(y1)
            y_coords.add(y2)

        events.sort()
        y_sorted = sorted(y_coords)
        y_idx = {y: i for i, y in enumerate(y_sorted)}

        # Count array: how many rectangles cover each y segment
        count = [0] * len(y_sorted)

        def calc_covered():
            """Calculate total covered y length"""
            total = 0
            for i in range(len(y_sorted) - 1):
                if count[i] > 0:
                    total += y_sorted[i + 1] - y_sorted[i]
            return total

        total_area = 0
        prev_x = events[0][0]

        for x, event_type, y1, y2 in events:
            # Add area from previous x to current x
            total_area += calc_covered() * (x - prev_x)
            total_area %= MOD

            # Update counts
            delta = 1 if event_type == 0 else -1
            for i in range(y_idx[y1], y_idx[y2]):
                count[i] += delta

            prev_x = x

        return total_area
