#1050. Actors and Directors Who Cooperated At Least Three Times
#Easy
#
#Table: ActorDirector
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| actor_id    | int     |
#| director_id | int     |
#| timestamp   | int     |
#+-------------+---------+
#timestamp is the primary key (column with unique values) for this table.
#
#Write a solution to find all the pairs (actor_id, director_id) where the
#actor has cooperated with the director at least three times.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#ActorDirector table:
#+-------------+-------------+-------------+
#| actor_id    | director_id | timestamp   |
#+-------------+-------------+-------------+
#| 1           | 1           | 0           |
#| 1           | 1           | 1           |
#| 1           | 1           | 2           |
#| 1           | 2           | 3           |
#| 1           | 2           | 4           |
#| 2           | 1           | 5           |
#| 2           | 1           | 6           |
#+-------------+-------------+-------------+
#Output:
#+-------------+-------------+
#| actor_id    | director_id |
#+-------------+-------------+
#| 1           | 1           |
#+-------------+-------------+
#Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

# SQL Solution:
#
# SELECT actor_id, director_id
# FROM ActorDirector
# GROUP BY actor_id, director_id
# HAVING COUNT(*) >= 3

# Python/Pandas Solution:
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """
    Find actor-director pairs with at least 3 cooperations.
    """
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    result = counts[counts['count'] >= 3][['actor_id', 'director_id']]
    return result


def actors_and_directors_alternative(actor_director: pd.DataFrame) -> pd.DataFrame:
    """Alternative using value_counts"""
    counts = actor_director.groupby(['actor_id', 'director_id']).agg(
        count=('timestamp', 'count')
    ).reset_index()

    return counts[counts['count'] >= 3][['actor_id', 'director_id']]
