#1488. Avoid Flood in The City
#Medium
#
#Your country has an infinite number of lakes. Initially, all the lakes are
#empty, but when it rains over the nth lake, the nth lake becomes full of water.
#If it rains over a lake that is full of water, there will be a flood. Your
#goal is to avoid floods in any lake.
#
#Given an integer array rains where:
#    rains[i] > 0 means there will be rains over the rains[i] lake.
#    rains[i] == 0 means there are no rains this day and you can choose one
#    lake this day and dry it.
#
#Return an array ans where:
#    ans[i] == -1 if rains[i] > 0.
#    ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
#
#If there are multiple valid answers return any of them. If it is impossible
#to avoid flood return an empty array.
#
#Example 1:
#Input: rains = [1,2,3,4]
#Output: [-1,-1,-1,-1]
#Explanation: After the first day full lakes are [1]
#After the second day full lakes are [1,2]
#After the third day full lakes are [1,2,3]
#After the fourth day full lakes are [1,2,3,4]
#There's no day to dry any lake and there is no flood in any lake.
#
#Example 2:
#Input: rains = [1,2,0,0,2,1]
#Output: [-1,-1,2,1,-1,-1]
#Explanation: After the first day full lakes are [1]
#After the second day full lakes are [1,2]
#After the third day, we dry lake 2. Full lakes are [1]
#After the fourth day, we dry lake 1. Full lakes are []
#After the fifth day full lakes are [2].
#After the sixth day full lakes are [1,2].
#It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another
#acceptable scenario.
#
#Example 3:
#Input: rains = [1,2,0,1,2]
#Output: []
#Explanation: After the second day, full lakes are [1,2]. We have to dry one
#lake in the third day. After that, it will rain over lakes [1,2]. It's easy
#to prove that no matter which lake you choose to dry in the 3rd day, the
#other one will flood.
#
#Constraints:
#    1 <= rains.length <= 10^5
#    0 <= rains[i] <= 10^9

from typing import List
from sortedcontainers import SortedList
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        Greedy with sorted dry days.
        When lake X rains again, use the earliest dry day AFTER last rain on X.
        """
        n = len(rains)
        result = [-1] * n

        # Track when each full lake was filled
        lake_filled_day = {}  # lake -> day it was filled

        # Available dry days (sorted)
        dry_days = SortedList()

        for day, lake in enumerate(rains):
            if lake == 0:
                # Dry day - save it for later use
                dry_days.add(day)
            else:
                # Rain on lake
                if lake in lake_filled_day:
                    # Lake is full, need to dry it
                    filled_day = lake_filled_day[lake]

                    # Find earliest dry day after filled_day
                    idx = dry_days.bisect_right(filled_day)

                    if idx == len(dry_days):
                        # No valid dry day available
                        return []

                    # Use this dry day to dry the lake
                    dry_day = dry_days[idx]
                    result[dry_day] = lake
                    dry_days.remove(dry_day)

                # Update when this lake was filled
                lake_filled_day[lake] = day

        # For unused dry days, dry any lake (use 1 as default)
        for day in dry_days:
            result[day] = 1

        return result


class SolutionBisect:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """Using standard library bisect (without sortedcontainers)"""
        n = len(rains)
        result = [-1] * n

        lake_filled_day = {}
        dry_days = []  # Sorted list of available dry days

        for day, lake in enumerate(rains):
            if lake == 0:
                bisect.insort(dry_days, day)
            else:
                if lake in lake_filled_day:
                    filled_day = lake_filled_day[lake]

                    # Find dry day after filled_day
                    idx = bisect.bisect_right(dry_days, filled_day)

                    if idx == len(dry_days):
                        return []

                    dry_day = dry_days.pop(idx)
                    result[dry_day] = lake

                lake_filled_day[lake] = day

        for day in dry_days:
            result[day] = 1

        return result


class SolutionPreprocess:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        Preprocess: find next rain day for each lake.
        Process dry days greedily - dry the lake with nearest next rain.
        """
        from collections import defaultdict
        import heapq

        n = len(rains)

        # For each lake, list all rain days (in order)
        lake_rain_days = defaultdict(list)
        for day, lake in enumerate(rains):
            if lake > 0:
                lake_rain_days[lake].append(day)

        # Convert to iterators
        lake_next_rain = {lake: iter(days) for lake, days in lake_rain_days.items()}

        result = [-1] * n
        full_lakes = {}  # lake -> day it will rain again (if known)

        # Min-heap of (next_rain_day, lake) for full lakes
        heap = []

        lake_indices = {lake: 0 for lake in lake_rain_days}

        for day, lake in enumerate(rains):
            if lake == 0:
                if not heap:
                    result[day] = 1  # Dry any lake
                else:
                    _, lake_to_dry = heapq.heappop(heap)
                    result[day] = lake_to_dry
                    del full_lakes[lake_to_dry]
            else:
                if lake in full_lakes:
                    return []  # Flood!

                # Lake becomes full
                # Find next rain day for this lake
                days_list = lake_rain_days[lake]
                idx = lake_indices[lake] + 1

                if idx < len(days_list):
                    next_rain = days_list[idx]
                    full_lakes[lake] = next_rain
                    heapq.heappush(heap, (next_rain, lake))
                else:
                    full_lakes[lake] = float('inf')

                lake_indices[lake] = idx

        return result
