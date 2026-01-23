#1294. Weather Type in Each Country
#Easy
#
#Table: Countries
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| country_id    | int     |
#| country_name  | varchar |
#+---------------+---------+
#country_id is the primary key for this table.
#
#Table: Weather
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| country_id    | int     |
#| weather_state | int     |
#| day           | date    |
#+---------------+---------+
#(country_id, day) is the primary key for this table.
#
#Write an SQL query to find the type of weather in each country for November 2019.
#The type of weather is:
#    Cold if the average weather_state is less than or equal 15,
#    Hot if the average weather_state is greater than or equal to 25, and
#    Warm otherwise.
#
#Return result table in any order.

# SQL Solution:
# SELECT c.country_name,
#     CASE
#         WHEN AVG(w.weather_state) <= 15 THEN 'Cold'
#         WHEN AVG(w.weather_state) >= 25 THEN 'Hot'
#         ELSE 'Warm'
#     END AS weather_type
# FROM Countries c
# JOIN Weather w ON c.country_id = w.country_id
# WHERE w.day BETWEEN '2019-11-01' AND '2019-11-30'
# GROUP BY c.country_id, c.country_name;

# Python simulation
from typing import List, Dict, Tuple
from collections import defaultdict
from datetime import date

class Solution:
    def weatherType(
        self,
        countries: List[Tuple[int, str]],
        weather: List[Tuple[int, int, date]]
    ) -> List[Tuple[str, str]]:
        """
        Classify weather by average temperature in November 2019.
        """
        # Create country name mapping
        country_names = {cid: name for cid, name in countries}

        # Filter and aggregate weather data for November 2019
        november_temps = defaultdict(list)
        for country_id, weather_state, day in weather:
            if day.year == 2019 and day.month == 11:
                november_temps[country_id].append(weather_state)

        # Classify each country
        result = []
        for country_id, temps in november_temps.items():
            avg_temp = sum(temps) / len(temps)

            if avg_temp <= 15:
                weather_type = 'Cold'
            elif avg_temp >= 25:
                weather_type = 'Hot'
            else:
                weather_type = 'Warm'

            result.append((country_names[country_id], weather_type))

        return result
