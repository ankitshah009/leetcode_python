#180. Consecutive Numbers
#Medium
#
#SQL Schema:
#Table: Logs
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| num         | varchar |
#+-------------+---------+
#id is the primary key for this table.
#id is an autoincrement column.
#
#Find all numbers that appear at least three times consecutively.
#Return the result table in any order.
#
#Example:
#Input:
#Logs table:
#+----+-----+
#| id | num |
#+----+-----+
#| 1  | 1   |
#| 2  | 1   |
#| 3  | 1   |
#| 4  | 2   |
#| 5  | 1   |
#| 6  | 2   |
#| 7  | 2   |
#+----+-----+
#Output:
#+-----------------+
#| ConsecutiveNums |
#+-----------------+
#| 1               |
#+-----------------+
#Explanation: 1 is the only number that appears consecutively for at least
#three times.

# SQL Solution using self-join:
"""
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.id = l2.id - 1
  AND l2.id = l3.id - 1
  AND l1.num = l2.num
  AND l2.num = l3.num;
"""

# SQL Solution using LAG/LEAD:
"""
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num) OVER (ORDER BY id) AS prev_num,
           LEAD(num) OVER (ORDER BY id) AS next_num
    FROM Logs
) t
WHERE num = prev_num AND num = next_num;
"""

# Pandas Solution:
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if len(logs) < 3:
        return pd.DataFrame({'ConsecutiveNums': []})

    logs = logs.sort_values('id')
    logs['prev'] = logs['num'].shift(1)
    logs['next'] = logs['num'].shift(-1)

    consecutive = logs[(logs['num'] == logs['prev']) & (logs['num'] == logs['next'])]

    result = consecutive['num'].drop_duplicates().reset_index(drop=True)
    return pd.DataFrame({'ConsecutiveNums': result})


def consecutive_numbers_rolling(logs: pd.DataFrame) -> pd.DataFrame:
    """Using rolling window approach"""
    if len(logs) < 3:
        return pd.DataFrame({'ConsecutiveNums': []})

    logs = logs.sort_values('id').reset_index(drop=True)
    consecutive = []

    for i in range(len(logs) - 2):
        if logs.loc[i, 'num'] == logs.loc[i+1, 'num'] == logs.loc[i+2, 'num']:
            consecutive.append(logs.loc[i, 'num'])

    return pd.DataFrame({'ConsecutiveNums': list(set(consecutive))})
