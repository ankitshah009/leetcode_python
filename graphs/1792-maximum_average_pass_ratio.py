#1792. Maximum Average Pass Ratio
#Medium
#
#There is a school that has classes of students and each class will be having a
#final exam. You are given a 2D integer array classes, where classes[i] =
#[passi, totali]. You know beforehand that in the ith class, there are totali
#total students, but only passi number of students will pass the exam.
#
#You are also given an integer extraStudents. There are another extraStudents
#brilliant students that are guaranteed to pass the exam of any class they are
#assigned to. You want to assign each of the extraStudents students to a class
#in a way that maximizes the average pass ratio across all the classes.
#
#The pass ratio of a class is equal to the number of students of the class that
#will pass the exam divided by the total number of students of the class. The
#average pass ratio is the sum of pass ratios of all the classes divided by the
#number of classes.
#
#Return the maximum possible average pass ratio after assigning the extraStudents
#students.
#
#Example 1:
#Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
#Output: 0.78333
#
#Example 2:
#Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
#Output: 0.53485
#
#Constraints:
#    1 <= classes.length <= 10^5
#    classes[i].length == 2
#    1 <= passi <= totali <= 10^5
#    1 <= extraStudents <= 10^5

from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        Greedy with max heap - always add student to class with maximum gain.
        Gain of adding one student: (p+1)/(t+1) - p/t
        """
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        # Max heap (negative for max behavior)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Calculate average
        return sum(p / t for _, p, t in heap) / len(classes)


class SolutionDetailed:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        Same approach with clearer explanation.
        """
        def delta(passed: int, total: int) -> float:
            """Improvement in ratio when adding one passing student."""
            return (passed + 1) / (total + 1) - passed / total

        # Priority queue: (-delta, passed, total)
        pq = [(-delta(p, t), p, t) for p, t in classes]
        heapq.heapify(pq)

        # Greedily assign extra students
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(pq)
            # Add one brilliant student
            new_p, new_t = p + 1, t + 1
            heapq.heappush(pq, (-delta(new_p, new_t), new_p, new_t))

        # Sum up ratios
        total_ratio = sum(p / t for _, p, t in pq)
        return total_ratio / len(classes)
