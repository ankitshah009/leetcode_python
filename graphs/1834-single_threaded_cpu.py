#1834. Single-Threaded CPU
#Medium
#
#You are given n tasks labeled from 0 to n - 1 represented by a 2D integer
#array tasks, where tasks[i] = [enqueueTime_i, processingTime_i] means that the
#ith task will be available to process at enqueueTime_i and will take
#processingTime_i to finish processing.
#
#You have a single-threaded CPU that can process at most one task at a time and
#will act in the following way:
#- If the CPU is idle and there are no available tasks to process, the CPU
#  remains idle.
#- If the CPU is idle and there are available tasks, the CPU will choose the
#  one with the shortest processing time. If multiple tasks have the same
#  shortest processing time, it will choose the task with the smallest index.
#- Once a task is started, the CPU will process the entire task without
#  stopping.
#- The CPU can finish a task then start a new one instantly.
#
#Return the order in which the CPU will process the tasks.
#
#Example 1:
#Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
#Output: [0,2,3,1]
#
#Example 2:
#Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
#Output: [4,3,2,0,1]
#
#Constraints:
#    tasks.length == n
#    1 <= n <= 10^5
#    1 <= enqueueTime_i, processingTime_i <= 10^9

from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        Simulation with min-heap sorted by (processingTime, index).
        """
        n = len(tasks)
        # Add original index to each task
        indexed_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        indexed_tasks.sort()  # Sort by enqueue time

        result = []
        heap = []  # (processingTime, index)
        time = 0
        task_idx = 0

        while len(result) < n:
            # Add all available tasks to heap
            while task_idx < n and indexed_tasks[task_idx][0] <= time:
                enqueue, process, idx = indexed_tasks[task_idx]
                heapq.heappush(heap, (process, idx))
                task_idx += 1

            if heap:
                # Process task with shortest time
                process_time, idx = heapq.heappop(heap)
                time += process_time
                result.append(idx)
            else:
                # Jump to next task's enqueue time
                time = indexed_tasks[task_idx][0]

        return result


class SolutionDetailed:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        Same approach with more explicit variable names.
        """
        n = len(tasks)

        # Create list of (enqueue_time, processing_time, original_index)
        task_list = []
        for i, (enqueue, process) in enumerate(tasks):
            task_list.append((enqueue, process, i))

        # Sort by enqueue time
        task_list.sort()

        result = []
        available = []  # Min-heap of (processing_time, original_index)
        current_time = 0
        i = 0

        while len(result) < n:
            # If no tasks available and heap empty, jump to next task
            if not available and i < n and task_list[i][0] > current_time:
                current_time = task_list[i][0]

            # Add all tasks that have arrived by current_time
            while i < n and task_list[i][0] <= current_time:
                enqueue, process, idx = task_list[i]
                heapq.heappush(available, (process, idx))
                i += 1

            # Process the task with shortest processing time
            if available:
                process_time, task_idx = heapq.heappop(available)
                current_time += process_time
                result.append(task_idx)

        return result
