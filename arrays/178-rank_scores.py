#178. Rank Scores
#Medium
#
#SQL Schema:
#Table: Scores
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| score       | decimal |
#+-------------+---------+
#id is the primary key for this table.
#
#Write a solution to find the rank of the scores. The ranking should be
#calculated according to the following rules:
#    The scores should be ranked from highest to lowest.
#    If there is a tie between two scores, both should have the same ranking.
#    After a tie, the next ranking number should be the next consecutive integer.
#
#Example:
#Input:
#Scores table:
#+----+-------+
#| id | score |
#+----+-------+
#| 1  | 3.50  |
#| 2  | 3.65  |
#| 3  | 4.00  |
#| 4  | 3.85  |
#| 5  | 4.00  |
#| 6  | 3.65  |
#+----+-------+
#Output:
#+-------+------+
#| score | rank |
#+-------+------+
#| 4.00  | 1    |
#| 4.00  | 1    |
#| 3.85  | 2    |
#| 3.65  | 3    |
#| 3.65  | 3    |
#| 3.50  | 4    |
#+-------+------+

# SQL Solution using DENSE_RANK:
"""
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as 'rank'
FROM Scores
ORDER BY score DESC;
"""

# Alternative SQL without window functions:
"""
SELECT s.score,
       (SELECT COUNT(DISTINCT s2.score)
        FROM Scores s2
        WHERE s2.score >= s.score) AS 'rank'
FROM Scores s
ORDER BY s.score DESC;
"""

# Pandas Solution:
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    result = scores[['score', 'rank']].sort_values('score', ascending=False)
    return result


def order_scores_alternative(scores: pd.DataFrame) -> pd.DataFrame:
    """Manual dense rank implementation"""
    sorted_scores = scores.sort_values('score', ascending=False)
    unique_scores = sorted_scores['score'].unique()
    rank_map = {score: rank + 1 for rank, score in enumerate(unique_scores)}
    sorted_scores['rank'] = sorted_scores['score'].map(rank_map)
    return sorted_scores[['score', 'rank']]
