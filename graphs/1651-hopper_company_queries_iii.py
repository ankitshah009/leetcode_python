#1651. Hopper Company Queries III
#Hard
#
#SQL Schema problem - implementing logic in Python
#
#Table: Drivers
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| driver_id   | int     |
#| join_date   | date    |
#+-------------+---------+
#
#Table: Rides
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| ride_id     | int     |
#| user_id     | int     |
#| requested_at| date    |
#+-------------+---------+
#
#Table: AcceptedRides
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| ride_id       | int     |
#| driver_id     | int     |
#| ride_distance | int     |
#| ride_duration | int     |
#+---------------+---------+
#
#Write a query to compute the average_ride_distance and average_ride_duration
#of every 3-month window starting from January - March 2020 to October - December 2020.
#Round average_ride_distance and average_ride_duration to 2 decimal places.

from typing import List, Dict
from collections import defaultdict

class Solution:
    def hopperCompanyQueriesIII(
        self,
        rides: List[Dict],
        accepted_rides: List[Dict]
    ) -> List[Dict]:
        """
        Calculate 3-month rolling averages for ride distance and duration.
        """
        # Build lookup for accepted rides
        accepted_lookup = {ar['ride_id']: ar for ar in accepted_rides}

        # Monthly aggregations for 2020
        monthly_distance = defaultdict(int)
        monthly_duration = defaultdict(int)

        for ride in rides:
            year = ride['requested_at'].year
            month = ride['requested_at'].month

            if year == 2020 and ride['ride_id'] in accepted_lookup:
                ar = accepted_lookup[ride['ride_id']]
                monthly_distance[month] += ar['ride_distance']
                monthly_duration[month] += ar['ride_duration']

        results = []

        # 3-month windows: Jan-Mar, Feb-Apr, ..., Oct-Dec
        for start_month in range(1, 11):
            total_distance = sum(monthly_distance[m] for m in range(start_month, start_month + 3))
            total_duration = sum(monthly_duration[m] for m in range(start_month, start_month + 3))

            results.append({
                'month': start_month,
                'average_ride_distance': round(total_distance / 3, 2),
                'average_ride_duration': round(total_duration / 3, 2)
            })

        return results


class SolutionDetailed:
    def hopperCompanyQueriesIII(
        self,
        drivers: List[Dict],
        rides: List[Dict],
        accepted_rides: List[Dict]
    ) -> List[Dict]:
        """
        More detailed implementation with data validation.
        """
        from datetime import date

        # Create ride_id to accepted_ride mapping
        ride_to_accepted = {}
        for ar in accepted_rides:
            ride_to_accepted[ar['ride_id']] = {
                'distance': ar['ride_distance'],
                'duration': ar['ride_duration']
            }

        # Aggregate by month for 2020
        monthly_stats = {m: {'distance': 0, 'duration': 0} for m in range(1, 13)}

        for ride in rides:
            req_date = ride['requested_at']
            if isinstance(req_date, str):
                req_date = date.fromisoformat(req_date)

            if req_date.year == 2020 and ride['ride_id'] in ride_to_accepted:
                month = req_date.month
                monthly_stats[month]['distance'] += ride_to_accepted[ride['ride_id']]['distance']
                monthly_stats[month]['duration'] += ride_to_accepted[ride['ride_id']]['duration']

        # Calculate 3-month rolling averages
        results = []
        for start in range(1, 11):
            window_months = [start, start + 1, start + 2]

            total_dist = sum(monthly_stats[m]['distance'] for m in window_months)
            total_dur = sum(monthly_stats[m]['duration'] for m in window_months)

            results.append({
                'month': start,
                'average_ride_distance': round(total_dist / 3, 2),
                'average_ride_duration': round(total_dur / 3, 2)
            })

        return results
