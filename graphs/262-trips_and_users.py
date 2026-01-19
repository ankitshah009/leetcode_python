#262. Trips and Users
#Hard
#
#SQL Schema:
#Table: Trips
#+-------------+----------+
#| Column Name | Type     |
#+-------------+----------+
#| id          | int      |
#| client_id   | int      |
#| driver_id   | int      |
#| city_id     | int      |
#| status      | enum     |
#| request_at  | date     |
#+-------------+----------+
#id is the primary key for this table.
#status is an ENUM ('completed', 'cancelled_by_driver', 'cancelled_by_client').
#
#Table: Users
#+-------------+----------+
#| Column Name | Type     |
#+-------------+----------+
#| users_id    | int      |
#| banned      | enum     |
#| role        | enum     |
#+-------------+----------+
#users_id is the primary key for this table.
#banned is an ENUM ('Yes', 'No').
#role is an ENUM ('client', 'driver', 'partner').
#
#The cancellation rate is computed by dividing the number of canceled (by client
#or driver) requests with unbanned users by the total number of requests with
#unbanned users on that day.
#
#Write a solution to find the cancellation rate of requests with unbanned users
#(both client and driver must not be banned) each day between "2013-10-01" and
#"2013-10-03". Round Cancellation Rate to two decimal points.
#
#Return the result table in any order.

# SQL Solution:
"""
SELECT t.request_at AS Day,
       ROUND(
           SUM(CASE WHEN t.status LIKE 'cancelled%' THEN 1 ELSE 0 END) /
           COUNT(*),
           2
       ) AS 'Cancellation Rate'
FROM Trips t
JOIN Users u1 ON t.client_id = u1.users_id AND u1.banned = 'No'
JOIN Users u2 ON t.driver_id = u2.users_id AND u2.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
"""

# Alternative SQL using subquery:
"""
SELECT request_at AS Day,
       ROUND(
           SUM(status != 'completed') / COUNT(*),
           2
       ) AS 'Cancellation Rate'
FROM Trips
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;
"""

# Pandas Solution:
import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Get unbanned users
    unbanned_users = users[users['banned'] == 'No']['users_id']

    # Filter trips: both client and driver must be unbanned
    valid_trips = trips[
        (trips['client_id'].isin(unbanned_users)) &
        (trips['driver_id'].isin(unbanned_users)) &
        (trips['request_at'] >= '2013-10-01') &
        (trips['request_at'] <= '2013-10-03')
    ]

    if valid_trips.empty:
        return pd.DataFrame({'Day': [], 'Cancellation Rate': []})

    # Calculate cancellation rate per day
    def calc_rate(group):
        total = len(group)
        cancelled = len(group[group['status'].str.startswith('cancelled')])
        return round(cancelled / total, 2) if total > 0 else 0.00

    result = valid_trips.groupby('request_at').apply(calc_rate).reset_index()
    result.columns = ['Day', 'Cancellation Rate']

    return result
