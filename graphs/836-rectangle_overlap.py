#836. Rectangle Overlap
#Easy
#
#An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where
#(x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the
#coordinate of its top-right corner. Its top and bottom edges are parallel to
#the X-axis, and its left and right edges are parallel to the Y-axis.
#
#Two rectangles overlap if the area of their intersection is positive. To be
#clear, two rectangles that only touch at the corner or edges do not overlap.
#
#Given two axis-aligned rectangles rec1 and rec2, return true if they overlap,
#otherwise return false.
#
#Example 1:
#Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
#Output: true
#
#Example 2:
#Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
#Output: false
#
#Example 3:
#Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
#Output: false
#
#Constraints:
#    rec1.length == 4
#    rec2.length == 4
#    -10^9 <= rec1[i], rec2[i] <= 10^9
#    rec1 and rec2 represent a valid rectangle with a non-zero area.

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        """
        Overlap exists if there's overlap in both x and y dimensions.
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        # Check x overlap: not (x2 <= x3 or x4 <= x1)
        x_overlap = x1 < x4 and x3 < x2

        # Check y overlap: not (y2 <= y3 or y4 <= y1)
        y_overlap = y1 < y4 and y3 < y2

        return x_overlap and y_overlap


class SolutionNoOverlap:
    """Check for no overlap conditions"""

    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # No overlap if one is completely to the left/right/above/below
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        # rec1 is to the left of rec2
        left = x2 <= x3
        # rec1 is to the right of rec2
        right = x1 >= x4
        # rec1 is below rec2
        below = y2 <= y3
        # rec1 is above rec2
        above = y1 >= y4

        return not (left or right or below or above)


class SolutionArea:
    """Check intersection area"""

    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        # Intersection rectangle
        inter_x1 = max(x1, x3)
        inter_y1 = max(y1, y3)
        inter_x2 = min(x2, x4)
        inter_y2 = min(y2, y4)

        # Check if intersection has positive area
        return inter_x1 < inter_x2 and inter_y1 < inter_y2
