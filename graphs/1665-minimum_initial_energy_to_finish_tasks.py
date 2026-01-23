#1665. Minimum Initial Energy to Finish Tasks
#Hard
#
#You are given an array tasks where tasks[i] = [actual_i, minimum_i]:
#- actual_i is the actual amount of energy you spend to finish the ith task.
#- minimum_i is the minimum amount of energy you require to begin the ith task.
#
#For example, if the task is [10, 12] and your current energy is 11, you cannot
#start this task. However, if your current energy is 13, you can complete this
#task, and your energy will be 3 after finishing it.
#
#You can finish the tasks in any order.
#
#Return the minimum initial amount of energy you will need to finish all the tasks.
#
#Example 1:
#Input: tasks = [[1,2],[2,4],[4,8]]
#Output: 8
#Explanation: Starting with 8 energy:
#  - 3rd task: 8 >= 8, finish with 8-4=4
#  - 2nd task: 4 >= 4, finish with 4-2=2
#  - 1st task: 2 >= 2, finish with 2-1=1
#
#Example 2:
#Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
#Output: 32
#
#Example 3:
#Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
#Output: 27
#
#Constraints:
#    1 <= tasks.length <= 10^5
#    1 <= actual_i <= minimum_i <= 10^4

from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        Greedy: Sort by (minimum - actual) in descending order.
        Tasks with larger "buffer" should come first.
        """
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        energy = 0
        total_actual = 0

        for actual, minimum in tasks:
            # We need at least max(minimum, total_actual + actual) energy
            energy = max(energy, total_actual + minimum)
            total_actual += actual

        return energy


class SolutionBinarySearch:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        Binary search for minimum initial energy.
        """
        def can_finish(initial: int) -> bool:
            """Check if we can finish all tasks with given initial energy."""
            energy = initial
            for actual, minimum in sorted(tasks, key=lambda x: x[1] - x[0], reverse=True):
                if energy < minimum:
                    return False
                energy -= actual
            return True

        # Binary search
        left = max(t[0] for t in tasks)  # At least max actual
        right = sum(t[1] for t in tasks)  # At most sum of all minimums

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left


class SolutionDP:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        Alternative greedy with explicit tracking.
        """
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        result = 0
        running_actual = 0

        for actual, minimum in tasks:
            # After doing previous tasks, we need at least 'minimum' now
            # Initial - running_actual >= minimum
            # Initial >= running_actual + minimum
            result = max(result, running_actual + minimum)
            running_actual += actual

        return result


class SolutionProof:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        With proof of greedy strategy.

        For two tasks (a1, m1) and (a2, m2):
        - Order 1 first: need max(m1, a1 + m2) initially
        - Order 2 first: need max(m2, a2 + m1) initially

        Order 1 first is better when:
        max(m1, a1 + m2) < max(m2, a2 + m1)

        This simplifies to: m1 - a1 > m2 - a2
        So sort by (minimum - actual) descending.
        """
        tasks.sort(key=lambda x: x[0] - x[1])  # Sort by actual - minimum ascending

        ans = 0
        cur = 0

        for actual, minimum in tasks:
            ans = max(ans, cur + minimum)
            cur += actual

        return ans


class SolutionAlternative:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        Think in terms of "extra energy needed" = minimum - actual.
        """
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        max_energy_needed = 0
        energy_spent = 0

        for actual, minimum in tasks:
            max_energy_needed = max(max_energy_needed, energy_spent + minimum)
            energy_spent += actual

        return max_energy_needed
