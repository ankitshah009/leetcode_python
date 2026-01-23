#1699. Number of Calls Between Two Persons
#Medium
#
#SQL Schema problem - implementing logic in Python
#
#Table: Calls
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| from_id     | int     |
#| to_id       | int     |
#| duration    | int     |
#+-------------+---------+
#This table does not have a primary key. It may contain duplicates.
#Each row of this table indicates a call between two persons.
#from_id != to_id
#
#Write a query to report the number of calls and the total call duration between
#each pair of distinct persons (person1, person2) where person1 < person2.

from typing import List, Dict
from collections import defaultdict

class Solution:
    def numberOfCalls(self, calls: List[Dict]) -> List[Dict]:
        """
        Aggregate calls between pairs, ensuring person1 < person2.
        """
        # Group by ordered pair
        pairs = defaultdict(lambda: {'count': 0, 'duration': 0})

        for call in calls:
            p1 = min(call['from_id'], call['to_id'])
            p2 = max(call['from_id'], call['to_id'])

            pairs[(p1, p2)]['count'] += 1
            pairs[(p1, p2)]['duration'] += call['duration']

        # Build result
        results = []
        for (p1, p2), stats in sorted(pairs.items()):
            results.append({
                'person1': p1,
                'person2': p2,
                'call_count': stats['count'],
                'total_duration': stats['duration']
            })

        return results


class SolutionSQL:
    """
    SQL equivalent:

    SELECT
        LEAST(from_id, to_id) AS person1,
        GREATEST(from_id, to_id) AS person2,
        COUNT(*) AS call_count,
        SUM(duration) AS total_duration
    FROM Calls
    GROUP BY person1, person2;

    -- Alternative:
    SELECT
        CASE WHEN from_id < to_id THEN from_id ELSE to_id END AS person1,
        CASE WHEN from_id < to_id THEN to_id ELSE from_id END AS person2,
        COUNT(*) AS call_count,
        SUM(duration) AS total_duration
    FROM Calls
    GROUP BY person1, person2;
    """
    pass


class SolutionPandas:
    def numberOfCalls(self, calls: List[Dict]) -> List[Dict]:
        """
        Pandas-style approach.
        """
        aggregated = defaultdict(lambda: [0, 0])

        for c in calls:
            key = tuple(sorted([c['from_id'], c['to_id']]))
            aggregated[key][0] += 1
            aggregated[key][1] += c['duration']

        return sorted([
            {
                'person1': k[0],
                'person2': k[1],
                'call_count': v[0],
                'total_duration': v[1]
            }
            for k, v in aggregated.items()
        ], key=lambda x: (x['person1'], x['person2']))


class SolutionCompact:
    def numberOfCalls(self, calls: List[Dict]) -> List[Dict]:
        """
        Compact implementation.
        """
        from collections import defaultdict

        d = defaultdict(lambda: [0, 0])
        for c in calls:
            k = (min(c['from_id'], c['to_id']), max(c['from_id'], c['to_id']))
            d[k][0] += 1
            d[k][1] += c['duration']

        return sorted([
            {'person1': k[0], 'person2': k[1], 'call_count': v[0], 'total_duration': v[1]}
            for k, v in d.items()
        ], key=lambda x: (x['person1'], x['person2']))
