#1376. Time Needed to Inform All Employees
#Medium
#
#A company has n employees with a unique ID for each employee from 0 to n - 1.
#The head of the company is the one with headID.
#
#Each employee has one direct manager given in the manager array where
#manager[i] is the direct manager of the i-th employee, manager[headID] = -1.
#Also, it is guaranteed that the subordination relationships have a tree structure.
#
#The head of the company wants to inform all the company employees of an urgent
#piece of news. He will inform his direct subordinates, and they will inform
#their subordinates, and so on until all employees know about the urgent news.
#
#The i-th employee needs informTime[i] minutes to inform all of his direct
#subordinates (i.e., After informTime[i] minutes, all his direct subordinates
#can start spreading the news).
#
#Return the number of minutes needed to inform all the employees about the urgent news.
#
#Example 1:
#Input: n = 1, headID = 0, manager = [-1], informTime = [0]
#Output: 0
#Explanation: The head of the company is the only employee in the company.
#
#Example 2:
#Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
#Output: 1
#
#Constraints:
#    1 <= n <= 10^5
#    0 <= headID < n
#    manager.length == n
#    0 <= manager[i] < n
#    manager[headID] == -1
#    informTime.length == n
#    0 <= informTime[i] <= 1000
#    informTime[i] == 0 if employee i has no subordinates.
#    It is guaranteed that all the employees can be informed.

from typing import List
from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        Build tree and find maximum path sum from root to any leaf.
        """
        # Build adjacency list (manager -> subordinates)
        subordinates = defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                subordinates[mgr].append(emp)

        # DFS to find max time
        def dfs(emp):
            if not subordinates[emp]:
                return 0
            return informTime[emp] + max(dfs(sub) for sub in subordinates[emp])

        return dfs(headID)


class SolutionBFS:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """BFS approach"""
        # Build tree
        subordinates = defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                subordinates[mgr].append(emp)

        max_time = 0
        queue = deque([(headID, 0)])  # (employee, time_to_receive_news)

        while queue:
            emp, time = queue.popleft()
            max_time = max(max_time, time)

            for sub in subordinates[emp]:
                queue.append((sub, time + informTime[emp]))

        return max_time


class SolutionBottomUp:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """Bottom-up: calculate time for each employee to be informed"""
        time_to_inform = [0] * n

        def get_time(emp):
            if time_to_inform[emp] > 0 or manager[emp] == -1:
                return time_to_inform[emp]

            time_to_inform[emp] = get_time(manager[emp]) + informTime[manager[emp]]
            return time_to_inform[emp]

        return max(get_time(emp) for emp in range(n))
