#621. Task Scheduler
#Medium
#
#You are given an array of CPU tasks, each represented by letters A to Z, and a
#cooling time n. Each cycle or interval allows the completion of one task. Tasks
#can be completed in any order, but there's a constraint: identical tasks must be
#separated by at least n intervals due to cooling time.
#
#Return the minimum number of intervals required to complete all tasks.
#
#Example 1:
#Input: tasks = ["A","A","A","B","B","B"], n = 2
#Output: 8
#Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
#
#Example 2:
#Input: tasks = ["A","A","A","B","B","B"], n = 0
#Output: 6
#
#Example 3:
#Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
#Output: 16
#
#Constraints:
#    1 <= tasks.length <= 10^4
#    tasks[i] is an uppercase English letter.
#    0 <= n <= 100

from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Mathematical approach based on max frequency task.
        Time: (max_freq - 1) * (n + 1) + count_of_max_freq_tasks
        """
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for f in freq.values() if f == max_freq)

        # Formula: (max_freq - 1) * (n + 1) + max_count
        # This accounts for the "frames" created by the most frequent task
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)


class SolutionHeap:
    """Simulation using max heap"""

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        while max_heap:
            cycle = []
            for _ in range(n + 1):
                if max_heap:
                    cycle.append(heapq.heappop(max_heap))

            for count in cycle:
                if count + 1 < 0:  # Still has remaining tasks
                    heapq.heappush(max_heap, count + 1)

            # If heap is empty, we just need the tasks we processed
            # Otherwise, we need the full cycle (n + 1)
            time += len(cycle) if not max_heap else n + 1

        return time


class SolutionQueue:
    """Using heap and cooldown queue"""

    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque

        freq = Counter(tasks)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # (count, available_time)

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Decrement (negative)
                if count < 0:
                    cooldown.append((count, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time
