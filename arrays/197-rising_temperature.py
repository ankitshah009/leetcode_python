#197. Rising Temperature
#Easy
#
#SQL Schema:
#Table: Weather
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| recordDate    | date    |
#| temperature   | int     |
#+---------------+---------+
#id is the primary key for this table.
#
#Write a solution to find all dates' Id with higher temperatures compared to
#its previous dates (yesterday).
#
#Example:
#Input:
#Weather table:
#+----+------------+-------------+
#| id | recordDate | temperature |
#+----+------------+-------------+
#| 1  | 2015-01-01 | 10          |
#| 2  | 2015-01-02 | 25          |
#| 3  | 2015-01-03 | 20          |
#| 4  | 2015-01-04 | 30          |
#+----+------------+-------------+
#Output:
#+----+
#| id |
#+----+
#| 2  |
#| 4  |
#+----+
#Explanation:
#On 2015-01-02, temperature was higher than on 2015-01-01 (25 > 10).
#On 2015-01-04, temperature was higher than on 2015-01-03 (30 > 20).

# SQL Solution 1: Using DATEDIFF
"""
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1
  AND w1.temperature > w2.temperature;
"""

# SQL Solution 2: Using DATE_SUB
"""
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON DATE_SUB(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
WHERE w1.temperature > w2.temperature;
"""

# SQL Solution 3: Using LAG window function
"""
SELECT id
FROM (
    SELECT id, temperature,
           LAG(temperature) OVER (ORDER BY recordDate) as prev_temp,
           LAG(recordDate) OVER (ORDER BY recordDate) as prev_date,
           recordDate
    FROM Weather
) t
WHERE temperature > prev_temp
  AND DATEDIFF(recordDate, prev_date) = 1;
"""

# Pandas Solution:
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Sort by date
    weather = weather.sort_values('recordDate')

    # Calculate date difference and temperature difference
    weather['prev_date'] = weather['recordDate'].shift(1)
    weather['prev_temp'] = weather['temperature'].shift(1)

    # Filter: temperature higher and exactly 1 day after
    rising = weather[
        (weather['temperature'] > weather['prev_temp']) &
        ((weather['recordDate'] - weather['prev_date']).dt.days == 1)
    ]

    return pd.DataFrame({'id': rising['id']})


def rising_temperature_merge(weather: pd.DataFrame) -> pd.DataFrame:
    """Using merge approach"""
    from datetime import timedelta

    weather['prev_date'] = weather['recordDate'] - timedelta(days=1)

    merged = weather.merge(
        weather[['recordDate', 'temperature']],
        left_on='prev_date',
        right_on='recordDate',
        suffixes=('', '_prev')
    )

    rising = merged[merged['temperature'] > merged['temperature_prev']]
    return pd.DataFrame({'id': rising['id']})
