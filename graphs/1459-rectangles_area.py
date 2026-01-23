#1459. Rectangles Area
#Medium
#
#Table: Points
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| x_value       | int     |
#| y_value       | int     |
#+---------------+---------+
#id is the primary key for this table.
#Each point is represented as a 2D coordinate (x_value, y_value).
#
#Write an SQL query to report all possible axis-aligned rectangles with a
#non-zero area that can be formed by any two points from the Points table.
#
#Each row in the result should contain three columns (p1, p2, area) where:
#    p1 and p2 are the id's of the two points that determine the opposite
#    corners of a rectangle.
#    area is the area of the rectangle and must be non-zero.
#
#Return the result table ordered by area in descending order. If there is a tie,
#order them by p1 in ascending order. If there is still a tie, order them by p2
#in ascending order.
#
#Example 1:
#Input:
#Points table:
#+----------+-------------+-------------+
#| id       | x_value     | y_value     |
#+----------+-------------+-------------+
#| 1        | 2           | 7           |
#| 2        | 4           | 8           |
#| 3        | 2           | 10          |
#+----------+-------------+-------------+
#Output:
#+----------+-------------+-------------+
#| p1       | p2          | area        |
#+----------+-------------+-------------+
#| 2        | 3           | 4           |
#| 1        | 2           | 2           |
#+----------+-------------+-------------+
#Explanation:
#The rectangle formed by p1 = 2 and p2 = 3 has an area equal to |4-2| * |8-10| = 4.
#The rectangle formed by p1 = 1 and p2 = 2 has an area equal to |2-4| * |7-8| = 2.
#Note that the rectangle formed by p1 = 1 and p2 = 3 is invalid because the area is 0.

#SQL Solution:
#SELECT
#    p1.id AS p1,
#    p2.id AS p2,
#    ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS area
#FROM Points p1
#JOIN Points p2 ON p1.id < p2.id
#WHERE p1.x_value != p2.x_value AND p1.y_value != p2.y_value
#ORDER BY area DESC, p1 ASC, p2 ASC;

from typing import List

class Solution:
    def rectanglesArea(self, points: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Find all pairs of points that form rectangles with non-zero area.
        """
        n = len(points)
        result = []

        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]

                # Rectangle needs different x and different y
                if p1['x_value'] != p2['x_value'] and p1['y_value'] != p2['y_value']:
                    area = abs(p1['x_value'] - p2['x_value']) * abs(p1['y_value'] - p2['y_value'])
                    result.append({
                        'p1': p1['id'],
                        'p2': p2['id'],
                        'area': area
                    })

        # Sort by area desc, then p1 asc, then p2 asc
        result.sort(key=lambda x: (-x['area'], x['p1'], x['p2']))

        return result


class SolutionExplicit:
    def rectanglesArea(self, points: List[dict]) -> List[dict]:
        """More explicit version"""
        rectangles = []

        # Generate all pairs
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]['x_value'], points[i]['y_value']
                x2, y2 = points[j]['x_value'], points[j]['y_value']

                # Calculate width and height
                width = abs(x1 - x2)
                height = abs(y1 - y2)

                # Area must be non-zero
                if width > 0 and height > 0:
                    area = width * height
                    rectangles.append({
                        'p1': points[i]['id'],
                        'p2': points[j]['id'],
                        'area': area
                    })

        # Sort as required
        rectangles.sort(key=lambda r: (-r['area'], r['p1'], r['p2']))

        return rectangles
