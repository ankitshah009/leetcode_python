#621. Task Scheduler
#Medium
#
#Given a characters array tasks, representing the tasks a CPU needs to do, where each letter
#represents a different task. Tasks could be done in any order. Each task is done in one unit
#of time. For each unit of time, the CPU could complete either one task or just be idle.
#
#However, there is a non-negative integer n that represents the cooldown period between two
#same tasks (the same letter in the array), that is that there must be at least n units of
#time between any two same tasks.
#
#Return the least number of units of times that the CPU will take to finish all the given tasks.
#
#Example 1:
#Input: tasks = ["A","A","A","B","B","B"], n = 2
#Output: 8
#Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
#
#Example 2:
#Input: tasks = ["A","A","A","B","B","B"], n = 0
#Output: 6
#Explanation: On this case any permutation of size 6 would work since n = 0.
#
#Example 3:
#Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
#Output: 16
#
#Constraints:
#    1 <= tasks.length <= 10^4
#    tasks[i] is upper-case English letter.
#    The integer n is in the range [0, 100].

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_count = max(count.values())

        # Count how many tasks have the maximum frequency
        num_max = sum(1 for c in count.values() if c == max_count)

        # Formula: (max_count - 1) * (n + 1) + num_max
        # This represents the minimum slots needed
        result = (max_count - 1) * (n + 1) + num_max

        # But we need at least len(tasks) slots
        return max(result, len(tasks))
