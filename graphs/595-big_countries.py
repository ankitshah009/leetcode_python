#595. Big Countries
#Easy
#
#Table: World
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| name        | varchar |
#| continent   | varchar |
#| area        | int     |
#| population  | int     |
#| gdp         | bigint  |
#+-------------+---------+
#name is the primary key column for this table.
#
#A country is big if:
#- it has an area of at least three million (i.e., 3000000 km^2), or
#- it has a population of at least twenty-five million (i.e., 25000000).
#
#Write a solution to find the name, population, and area of the big countries.
#Return the result table in any order.

# SQL Solution:
# SELECT name, population, area
# FROM World
# WHERE area >= 3000000 OR population >= 25000000;

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """Pandas solution"""
    big = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return big[['name', 'population', 'area']]


def big_countries_query(world: pd.DataFrame) -> pd.DataFrame:
    """Using query method"""
    return world.query('area >= 3000000 or population >= 25000000')[['name', 'population', 'area']]
