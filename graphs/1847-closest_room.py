#1847. Closest Room
#Hard
#
#There is a hotel with n rooms. The rooms are represented by a 2D integer array
#rooms where rooms[i] = [roomId_i, size_i] denotes that there is a room with
#room number roomId_i and size size_i. Each roomId_i is guaranteed to be
#unique.
#
#You are also given k queries in a 2D array queries where
#queries[j] = [preferred_j, minSize_j]. The answer to the jth query is the room
#number id of a room such that:
#- The room has a size of at least minSize_j, and
#- abs(id - preferred_j) is minimized.
#
#If there is a tie, use the room with the smallest id. If there is no such
#room, the answer is -1.
#
#Return an array answer of length k where answer[j] contains the answer to the
#jth query.
#
#Example 1:
#Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
#Output: [3,-1,3]
#
#Example 2:
#Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]],
#       queries = [[2,3],[2,4],[2,5]]
#Output: [2,1,3]
#
#Constraints:
#    n == rooms.length
#    1 <= n <= 10^5
#    k == queries.length
#    1 <= k <= 10^4
#    1 <= roomId_i, preferred_j <= 10^7
#    1 <= size_i, minSize_j <= 10^7

from typing import List
from sortedcontainers import SortedList
import bisect

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Offline processing: sort queries by minSize descending,
        add rooms to sorted structure as they become eligible.
        """
        # Sort rooms by size descending
        rooms.sort(key=lambda x: -x[1])

        # Add query index and sort by minSize descending
        indexed_queries = [(minSize, preferred, i)
                          for i, (preferred, minSize) in enumerate(queries)]
        indexed_queries.sort(reverse=True)

        result = [-1] * len(queries)
        available_ids = SortedList()
        room_idx = 0

        for minSize, preferred, query_idx in indexed_queries:
            # Add all rooms with size >= minSize
            while room_idx < len(rooms) and rooms[room_idx][1] >= minSize:
                available_ids.add(rooms[room_idx][0])
                room_idx += 1

            if not available_ids:
                continue

            # Find closest room id to preferred
            pos = available_ids.bisect_left(preferred)

            candidates = []
            if pos < len(available_ids):
                candidates.append(available_ids[pos])
            if pos > 0:
                candidates.append(available_ids[pos - 1])

            # Choose closest (smaller id on tie)
            best = min(candidates, key=lambda x: (abs(x - preferred), x))
            result[query_idx] = best

        return result


class SolutionBinarySearch:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Same approach with explicit binary search.
        """
        rooms.sort(key=lambda x: -x[1])

        q = len(queries)
        indexed_queries = sorted(range(q),
                                  key=lambda i: -queries[i][1])

        result = [-1] * q
        room_ids = SortedList()
        j = 0

        for i in indexed_queries:
            preferred, minSize = queries[i]

            # Add eligible rooms
            while j < len(rooms) and rooms[j][1] >= minSize:
                room_ids.add(rooms[j][0])
                j += 1

            if not room_ids:
                continue

            # Binary search for closest
            idx = room_ids.bisect_left(preferred)

            best_id = -1
            best_dist = float('inf')

            for k in [idx - 1, idx]:
                if 0 <= k < len(room_ids):
                    dist = abs(room_ids[k] - preferred)
                    if dist < best_dist or (dist == best_dist and room_ids[k] < best_id):
                        best_dist = dist
                        best_id = room_ids[k]

            result[i] = best_id

        return result
