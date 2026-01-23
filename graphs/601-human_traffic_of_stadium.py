#601. Human Traffic of Stadium
#Hard
#
#Table: Stadium
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| visit_date    | date    |
#| people        | int     |
#+---------------+---------+
#visit_date is the primary key.
#
#Write a solution to display the records with three or more rows with consecutive
#id's, and the number of people is greater than or equal to 100 for each.
#Return the result table ordered by visit_date in ascending order.

# SQL Solution:
# WITH crowded AS (
#     SELECT *,
#            id - ROW_NUMBER() OVER (ORDER BY id) AS grp
#     FROM Stadium
#     WHERE people >= 100
# )
# SELECT id, visit_date, people
# FROM crowded
# WHERE grp IN (
#     SELECT grp FROM crowded
#     GROUP BY grp
#     HAVING COUNT(*) >= 3
# )
# ORDER BY visit_date;

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    """Pandas solution using grouping technique"""
    # Filter rows with people >= 100
    crowded = stadium[stadium['people'] >= 100].copy()

    if len(crowded) < 3:
        return pd.DataFrame(columns=['id', 'visit_date', 'people'])

    # Create group identifier using id difference from row number
    crowded['grp'] = crowded['id'] - range(len(crowded))

    # Find groups with 3+ consecutive rows
    group_counts = crowded.groupby('grp').size()
    valid_groups = group_counts[group_counts >= 3].index

    # Filter and return
    result = crowded[crowded['grp'].isin(valid_groups)]
    return result[['id', 'visit_date', 'people']].sort_values('visit_date')
