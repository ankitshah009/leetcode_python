#1661. Average Time of Process per Machine
#Easy
#
#SQL Schema problem - implementing logic in Python
#
#Table: Activity
#+----------------+---------+
#| Column Name    | Type    |
#+----------------+---------+
#| machine_id     | int     |
#| process_id     | int     |
#| activity_type  | enum    |
#| timestamp      | float   |
#+----------------+---------+
#(machine_id, process_id, activity_type) is the primary key.
#activity_type is ENUM ('start', 'end').
#
#Write a query to find the average time each machine takes to complete a process.
#The time to complete a process is the 'end' timestamp minus the 'start' timestamp.
#The average time is calculated by the total time to complete every process on
#the machine divided by the number of processes that were run.
#
#The result table should have the machine_id along with the average time as
#processing_time, which should be rounded to 3 decimal places.

from typing import List, Dict
from collections import defaultdict

class Solution:
    def averageTime(self, activities: List[Dict]) -> List[Dict]:
        """
        Calculate average processing time per machine.
        """
        # Group by machine_id and process_id
        processes = defaultdict(dict)  # {(machine_id, process_id): {'start': t, 'end': t}}

        for activity in activities:
            key = (activity['machine_id'], activity['process_id'])
            processes[key][activity['activity_type']] = activity['timestamp']

        # Calculate total time per machine
        machine_times = defaultdict(list)

        for (machine_id, _), times in processes.items():
            if 'start' in times and 'end' in times:
                duration = times['end'] - times['start']
                machine_times[machine_id].append(duration)

        # Calculate averages
        results = []
        for machine_id in sorted(machine_times.keys()):
            times = machine_times[machine_id]
            avg = sum(times) / len(times)
            results.append({
                'machine_id': machine_id,
                'processing_time': round(avg, 3)
            })

        return results


class SolutionPandas:
    def averageTime(self, activities: List[Dict]) -> List[Dict]:
        """
        Using pandas-like approach.
        """
        # Separate start and end activities
        starts = {}
        ends = {}

        for a in activities:
            key = (a['machine_id'], a['process_id'])
            if a['activity_type'] == 'start':
                starts[key] = a['timestamp']
            else:
                ends[key] = a['timestamp']

        # Calculate durations
        durations = defaultdict(list)
        for key in starts:
            if key in ends:
                duration = ends[key] - starts[key]
                durations[key[0]].append(duration)

        # Calculate averages
        return [
            {
                'machine_id': mid,
                'processing_time': round(sum(times) / len(times), 3)
            }
            for mid, times in sorted(durations.items())
        ]


class SolutionSQL:
    """
    SQL equivalent:

    SELECT
        machine_id,
        ROUND(AVG(end_time - start_time), 3) AS processing_time
    FROM (
        SELECT
            a1.machine_id,
            a1.process_id,
            a1.timestamp AS start_time,
            a2.timestamp AS end_time
        FROM Activity a1
        JOIN Activity a2
            ON a1.machine_id = a2.machine_id
            AND a1.process_id = a2.process_id
            AND a1.activity_type = 'start'
            AND a2.activity_type = 'end'
    ) sub
    GROUP BY machine_id;
    """
    pass


class SolutionCompact:
    def averageTime(self, activities: List[Dict]) -> List[Dict]:
        """
        Compact implementation.
        """
        from collections import defaultdict

        data = defaultdict(lambda: defaultdict(dict))

        for a in activities:
            data[a['machine_id']][a['process_id']][a['activity_type']] = a['timestamp']

        results = []
        for mid in sorted(data.keys()):
            durations = [
                p['end'] - p['start']
                for p in data[mid].values()
                if 'start' in p and 'end' in p
            ]
            if durations:
                results.append({
                    'machine_id': mid,
                    'processing_time': round(sum(durations) / len(durations), 3)
                })

        return results
