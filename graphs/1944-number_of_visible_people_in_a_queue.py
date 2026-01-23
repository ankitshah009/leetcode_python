#1944. Number of Visible People in a Queue
#Hard
#
#There are n people standing in a queue, and they numbered from 0 to n - 1 in
#left to right order. You are given an array heights of distinct integers where
#heights[i] represents the height of the ith person.
#
#A person can see another person to their right in the queue if everybody in
#between is shorter than both of them. More formally, the ith person can see
#the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1],
#heights[i+2], ..., heights[j-1]).
#
#Return an array answer of length n where answer[i] is the number of people the
#ith person can see to their right in the queue.
#
#Example 1:
#Input: heights = [10,6,8,5,11,9]
#Output: [3,1,2,1,1,0]
#
#Example 2:
#Input: heights = [5,1,2,3,10]
#Output: [4,1,1,1,0]
#
#Constraints:
#    n == heights.length
#    1 <= n <= 10^5
#    1 <= heights[i] <= 10^5
#    All the values of heights are unique.

from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        Monotonic stack from right to left.
        Count people popped + 1 if stack not empty after.
        """
        n = len(heights)
        result = [0] * n
        stack = []  # Decreasing stack of heights

        for i in range(n - 1, -1, -1):
            count = 0

            # Pop all shorter people (current person can see them)
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1

            # If stack not empty, current person can also see the next taller
            if stack:
                count += 1

            result[i] = count
            stack.append(heights[i])

        return result


class SolutionLeftToRight:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        Process left to right, stack stores indices.
        """
        n = len(heights)
        result = [0] * n
        stack = []  # Stack of indices with decreasing heights

        for i in range(n):
            # Current person blocks view for shorter people in stack
            while stack and heights[stack[-1]] < heights[i]:
                j = stack.pop()
                result[j] += 1

            # Top of stack (if exists) can see current person
            if stack:
                result[stack[-1]] += 1

            stack.append(i)

        return result
