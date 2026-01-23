#1501. Countries You Can Safely Invest In
#Medium (SQL)
#
#Table Person:
#+----------------+---------+
#| Column Name    | Type    |
#+----------------+---------+
#| id             | int     |
#| name           | varchar |
#| phone_number   | varchar |
#+----------------+---------+
#id is the primary key for this table.
#Each row of this table contains the name of a person and their phone number.
#Phone number will be in the form 'xxx-yyyyyyy' where xxx is the country code
#(3 characters) and yyyyyyy is the phone number (7 characters).
#
#Table Country:
#+----------------+---------+
#| Column Name    | Type    |
#+----------------+---------+
#| name           | varchar |
#| country_code   | varchar |
#+----------------+---------+
#country_code is the primary key for this table.
#Each row of this table contains the country name and its code.
#
#Table Calls:
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| caller_id   | int     |
#| callee_id   | int     |
#| duration    | int     |
#+-------------+---------+
#There is no primary key for this table, it may contain duplicates.
#Each row of this table contains the caller id, callee id and the duration of
#the call in minutes.
#
#A telecommunications company wants to invest in new countries. The company
#intends to invest in the countries where the average call duration of the
#calls in this country is strictly greater than the global average call duration.
#
#Write an SQL query to find the countries where this company can invest.
#
#Return the result table in any order.

#SQL Solution:
#WITH call_data AS (
#    SELECT c.caller_id AS person_id, c.duration
#    FROM Calls c
#    UNION ALL
#    SELECT c.callee_id AS person_id, c.duration
#    FROM Calls c
#),
#country_calls AS (
#    SELECT
#        co.name AS country,
#        cd.duration
#    FROM call_data cd
#    JOIN Person p ON cd.person_id = p.id
#    JOIN Country co ON SUBSTRING(p.phone_number, 1, 3) = co.country_code
#)
#SELECT country
#FROM country_calls
#GROUP BY country
#HAVING AVG(duration) > (SELECT AVG(duration) FROM Calls);

from typing import List

class Solution:
    def countriesSafeToInvest(self, persons: List[dict], countries: List[dict],
                              calls: List[dict]) -> List[str]:
        """
        Python simulation of SQL query.
        Find countries with average call duration > global average.
        """
        if not calls:
            return []

        # Create lookup maps
        person_phone = {p['id']: p['phone_number'] for p in persons}
        code_to_country = {c['country_code']: c['name'] for c in countries}

        def get_country(person_id: int) -> str:
            phone = person_phone.get(person_id, '')
            code = phone[:3] if phone else ''
            return code_to_country.get(code, '')

        # Calculate global average
        global_avg = sum(c['duration'] for c in calls) / len(calls)

        # Collect call durations by country
        from collections import defaultdict
        country_durations = defaultdict(list)

        for call in calls:
            # Both caller and callee contribute
            caller_country = get_country(call['caller_id'])
            callee_country = get_country(call['callee_id'])

            if caller_country:
                country_durations[caller_country].append(call['duration'])
            if callee_country:
                country_durations[callee_country].append(call['duration'])

        # Find countries with avg > global avg
        result = []
        for country, durations in country_durations.items():
            if durations:
                avg = sum(durations) / len(durations)
                if avg > global_avg:
                    result.append(country)

        return result


class SolutionExplicit:
    def countriesSafeToInvest(self, persons: List[dict], countries: List[dict],
                              calls: List[dict]) -> List[str]:
        """More explicit step-by-step solution"""
        from collections import defaultdict

        # Step 1: Build lookup tables
        person_to_country = {}
        code_to_country = {c['country_code']: c['name'] for c in countries}

        for person in persons:
            country_code = person['phone_number'][:3]
            person_to_country[person['id']] = code_to_country.get(country_code)

        # Step 2: Calculate global average
        if not calls:
            return []

        total_duration = sum(c['duration'] for c in calls)
        global_avg = total_duration / len(calls)

        # Step 3: Aggregate by country (both caller and callee)
        country_stats = defaultdict(lambda: {'total': 0, 'count': 0})

        for call in calls:
            duration = call['duration']

            # Caller's country
            caller_country = person_to_country.get(call['caller_id'])
            if caller_country:
                country_stats[caller_country]['total'] += duration
                country_stats[caller_country]['count'] += 1

            # Callee's country
            callee_country = person_to_country.get(call['callee_id'])
            if callee_country:
                country_stats[callee_country]['total'] += duration
                country_stats[callee_country]['count'] += 1

        # Step 4: Find countries exceeding global average
        result = []
        for country, stats in country_stats.items():
            if stats['count'] > 0:
                country_avg = stats['total'] / stats['count']
                if country_avg > global_avg:
                    result.append(country)

        return result
