#1606. Find Servers That Handled Most Number of Requests
#Hard
#
#You have k servers numbered from 0 to k-1 that are being used to handle
#multiple requests simultaneously. Each server has infinite computational
#capacity but cannot handle more than one request at a time. The requests are
#assigned to servers according to a specific algorithm:
#
#- The ith (0-indexed) request arrives.
#- If all servers are busy, the request is dropped (not handled at all).
#- If the (i % k)th server is available, assign the request to that server.
#- Otherwise, assign the request to the next available server (wrapping around
#  the list of servers and starting from 0 if necessary). For example, if the
#  ith server is busy, try to assign the request to the (i+1)th server, then
#  the (i+2)th server, and so on.
#
#You are given a strictly increasing array arrival of positive integers, where
#arrival[i] represents the arrival time of the ith request, and another array
#load, where load[i] represents the load of the ith request (the time it takes
#to complete). Your goal is to find the busiest server(s). A server is considered
#busiest if it handled the most number of requests successfully among all the servers.
#
#Return a list containing the IDs (0-indexed) of the busiest server(s). You may
#return the IDs in any order.
#
#Example 1:
#Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]
#Output: [1]
#Explanation:
#All of the servers start out available.
#The first 3 requests are handled by the first 3 servers in order.
#Request 3 comes in. Server 0 is busy, so it's assigned to server 1.
#Request 4 comes in. Servers 0, 1, 2 are all busy, so the request is dropped.
#Servers 0 and 2 handled one request each, while server 1 handled two requests.
#Hence server 1 is the busiest server.
#
#Example 2:
#Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
#Output: [0]
#
#Example 3:
#Input: k = 3, arrival = [1,2,3], load = [10,12,11]
#Output: [0,1,2]
#
#Constraints:
#    1 <= k <= 10^5
#    1 <= arrival.length, load.length <= 10^5
#    arrival.length == load.length
#    1 <= arrival[i], load[i] <= 10^9
#    arrival is strictly increasing.

from typing import List
import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
        Use a min-heap for busy servers (by end time) and a sorted set for available servers.

        For each request:
        1. Free up servers whose tasks have completed
        2. Find the next available server >= i % k (wrap around if needed)
        3. Assign the request to that server
        """
        # available[j] means server j is available
        available = SortedList(range(k))

        # Min-heap: (end_time, server_id)
        busy = []

        # Count requests handled by each server
        count = [0] * k

        for i, (arrive, duration) in enumerate(zip(arrival, load)):
            # Free up servers that have finished
            while busy and busy[0][0] <= arrive:
                _, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue  # Drop request

            # Find server >= (i % k), or wrap around
            target = i % k
            idx = available.bisect_left(target)

            if idx == len(available):
                idx = 0  # Wrap around to first available

            server = available[idx]
            available.remove(server)

            heapq.heappush(busy, (arrive + duration, server))
            count[server] += 1

        # Find busiest servers
        max_count = max(count)
        return [i for i in range(k) if count[i] == max_count]


class SolutionTwoHeaps:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
        Using two heaps: one for busy servers, one for available servers.

        The trick for handling circular wrap-around is to store
        server IDs as (server_id + n*k) in the available heap where n
        increments to handle the modular arithmetic properly.
        """
        # Available servers as min-heap
        available = list(range(k))  # Initially all available
        heapq.heapify(available)

        # Busy servers: (end_time, server_id)
        busy = []

        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Release servers that finished before this request
            while busy and busy[0][0] <= start:
                end_time, server = heapq.heappop(busy)
                # Add server back, but offset to handle wrap-around
                # We add i // k * k + server to ensure correct modular search
                heapq.heappush(available, i // k * k + server + (k if server < i % k else 0))

            if not available:
                continue

            # Get next available server
            server_raw = heapq.heappop(available)
            server = server_raw % k

            count[server] += 1
            heapq.heappush(busy, (start + duration, server))

        max_requests = max(count)
        return [i for i in range(k) if count[i] == max_requests]


class SolutionSimple:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
        Simpler O(n*k) approach for smaller inputs.
        """
        # end_time[i] = when server i becomes free
        end_time = [0] * k
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Find first available server starting from i % k
            found = False
            for offset in range(k):
                server = (i % k + offset) % k
                if end_time[server] <= start:
                    end_time[server] = start + duration
                    count[server] += 1
                    found = True
                    break

            # If not found, request is dropped

        max_count = max(count)
        return [i for i in range(k) if count[i] == max_count]
