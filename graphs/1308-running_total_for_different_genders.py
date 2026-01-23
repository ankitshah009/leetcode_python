#1308. Running Total for Different Genders
#Medium
#
#Table: Scores
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| player_name   | varchar |
#| gender        | varchar |
#| day           | date    |
#| score_points  | int     |
#+---------------+---------+
#(gender, day) is the primary key for this table.
#A competition is held between the female team and the male team.
#Each row of this table indicates that a player_name and with gender has scored
#score_point in someday.
#Gender is 'F' if the player is in the female team and 'M' if the player is in
#the male team.
#
#Write an SQL query to find the total score for each gender on each day.
#
#Return the result table ordered by gender and day in ascending order.
#
#Example 1:
#Input:
#Scores table:
#+-------------+--------+------------+--------------+
#| player_name | gender | day        | score_points |
#+-------------+--------+------------+--------------+
#| Aron        | F      | 2020-01-01 | 17           |
#| Alice       | F      | 2020-01-07 | 23           |
#| Bajeli      | M      | 2020-01-07 | 7            |
#| Kheli       | M      | 2019-12-25 | 11           |
#| Slaman      | M      | 2019-12-30 | 13           |
#| Joe         | M      | 2019-12-31 | 3            |
#| Jose        | M      | 2019-12-18 | 2            |
#| Priya       | F      | 2019-12-31 | 23           |
#| Priyanka    | F      | 2019-12-30 | 17           |
#+-------------+--------+------------+--------------+
#Output:
#+--------+------------+-------+
#| gender | day        | total |
#+--------+------------+-------+
#| F      | 2019-12-30 | 17    |
#| F      | 2019-12-31 | 40    |
#| F      | 2020-01-01 | 57    |
#| F      | 2020-01-07 | 80    |
#| M      | 2019-12-18 | 2     |
#| M      | 2019-12-25 | 13    |
#| M      | 2019-12-30 | 26    |
#| M      | 2019-12-31 | 29    |
#| M      | 2020-01-07 | 36    |
#+--------+------------+-------+

# SQL Solution using window function:
# SELECT gender, day,
#     SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total
# FROM Scores
# ORDER BY gender, day;

# SQL Solution using self-join:
# SELECT s1.gender, s1.day,
#     SUM(s2.score_points) AS total
# FROM Scores s1
# JOIN Scores s2 ON s1.gender = s2.gender AND s1.day >= s2.day
# GROUP BY s1.gender, s1.day
# ORDER BY s1.gender, s1.day;

# Python simulation
from typing import List, Tuple
from datetime import date
from collections import defaultdict

class Solution:
    def runningTotal(
        self,
        scores: List[Tuple[str, str, date, int]]
    ) -> List[Tuple[str, date, int]]:
        """
        Calculate running total of scores by gender.
        """
        # Group by gender and sort by date
        by_gender = defaultdict(list)
        for player, gender, day, points in scores:
            by_gender[gender].append((day, points))

        result = []

        for gender in sorted(by_gender.keys()):
            entries = sorted(by_gender[gender], key=lambda x: x[0])

            # Aggregate same-day scores
            day_scores = defaultdict(int)
            for day, points in entries:
                day_scores[day] += points

            # Calculate running total
            running = 0
            for day in sorted(day_scores.keys()):
                running += day_scores[day]
                result.append((gender, day, running))

        return result
