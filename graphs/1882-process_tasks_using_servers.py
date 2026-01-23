#1882. Process Tasks Using Servers
#Medium
#
#You are given two 0-indexed integer arrays servers and tasks of lengths n and
#m respectively. servers[i] is the weight of the ith server, and tasks[j] is
#the time needed to process the jth task in seconds.
#
#Tasks are assigned to the servers using a task queue. Initially, all servers
#are free, and the queue is empty.
#
#At second j, the jth task is inserted into the queue. As long as there are
#free servers and the queue is not empty, the task in the front of the queue
#will be assigned to a free server with the smallest weight, and in case of a
#tie, choose the server with the smallest index.
#
#If there are no free servers and the queue is not empty, we wait until a
#server becomes free and immediately assign the next task. If multiple servers
#become free at the same time, then multiple tasks from the queue are assigned
#in order of insertion.
#
#A server that is assigned task j at second t will be free again at second
#t + tasks[j].
#
#Return an array ans of length m, where ans[j] is the index of the server that
#the jth task will be assigned to.
#
#Example 1:
#Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
#Output: [2,2,0,2,1,2]
#
#Example 2:
#Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
#Output: [1,4,1,4,1,3,2]
#
#Constraints:
#    servers.length == n
#    tasks.length == m
#    1 <= n, m <= 2 * 10^5
#    1 <= servers[i], tasks[j] <= 2 * 10^5

from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        Use two heaps: free servers and busy servers.
        """
        n, m = len(servers), len(tasks)

        # Free servers: (weight, index)
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)

        # Busy servers: (free_time, weight, index)
        busy = []

        result = []
        time = 0

        for j in range(m):
            time = max(time, j)

            # Free up servers that finished
            while busy and busy[0][0] <= time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # If no free server, wait for first to free up
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] == time:
                    _, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            # Assign task to best free server
            weight, server_idx = heapq.heappop(free)
            result.append(server_idx)

            # Mark server as busy
            heapq.heappush(busy, (time + tasks[j], weight, server_idx))

        return result


class SolutionDetailed:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        Same approach with detailed comments.
        """
        # free: min-heap of (weight, index) for available servers
        # busy: min-heap of (end_time, weight, index) for busy servers

        free = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free)

        busy = []
        result = []

        for task_idx, task_time in enumerate(tasks):
            # Current time is at least task_idx (when task arrives)
            current_time = task_idx

            # Move finished servers from busy to free
            while busy and busy[0][0] <= current_time:
                end_time, weight, server_idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, server_idx))

            # If no free servers, jump to when first becomes free
            if not free:
                current_time = busy[0][0]
                while busy and busy[0][0] == current_time:
                    _, weight, server_idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, server_idx))

            # Assign to best available server
            weight, server_idx = heapq.heappop(free)
            result.append(server_idx)

            # Server becomes busy
            end_time = current_time + task_time
            heapq.heappush(busy, (end_time, weight, server_idx))

        return result
