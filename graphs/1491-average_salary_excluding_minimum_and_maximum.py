#1491. Average Salary Excluding the Minimum and Maximum Salary
#Easy
#
#You are given an array of unique integers salary where salary[i] is the salary
#of the ith employee.
#
#Return the average salary of employees excluding the minimum and maximum salary.
#Answers within 10^-5 of the actual answer will be accepted.
#
#Example 1:
#Input: salary = [4000,3000,1000,2000]
#Output: 2500.00000
#Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
#Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
#
#Example 2:
#Input: salary = [1000,2000,3000]
#Output: 2000.00000
#Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
#Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
#
#Constraints:
#    3 <= salary.length <= 100
#    1000 <= salary[i] <= 10^6
#    All the integers of salary are unique.

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        """
        Sum all, subtract min and max, divide by (n-2).
        """
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


class SolutionOnePass:
    def average(self, salary: List[int]) -> float:
        """Single pass tracking min, max, and sum"""
        total = 0
        min_sal = float('inf')
        max_sal = float('-inf')

        for s in salary:
            total += s
            min_sal = min(min_sal, s)
            max_sal = max(max_sal, s)

        return (total - min_sal - max_sal) / (len(salary) - 2)


class SolutionSort:
    def average(self, salary: List[int]) -> float:
        """Sort and sum middle elements"""
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)


class SolutionHeap:
    def average(self, salary: List[int]) -> float:
        """Using heap to find min and max"""
        import heapq

        min_sal = heapq.nsmallest(1, salary)[0]
        max_sal = heapq.nlargest(1, salary)[0]

        return (sum(salary) - min_sal - max_sal) / (len(salary) - 2)


class SolutionStatistics:
    def average(self, salary: List[int]) -> float:
        """Using statistics module (for demonstration)"""
        # Note: This doesn't exactly match the problem but shows statistics usage
        # The problem wants to exclude exact min and max, not trimmed mean

        total = sum(salary)
        min_sal = min(salary)
        max_sal = max(salary)

        return (total - min_sal - max_sal) / (len(salary) - 2)
