#1700. Number of Students Unable to Eat Lunch
#Easy
#
#The school cafeteria offers circular and square sandwiches at lunch break,
#referred to by numbers 0 and 1 respectively. All students stand in a queue.
#Each student either prefers square or circular sandwiches.
#
#The number of sandwiches in the cafeteria is equal to the number of students.
#The sandwiches are placed in a stack. At each step:
#- If the student at the front of the queue prefers the sandwich on top of the
#  stack, they will take it and leave the queue.
#- Otherwise, they will leave it and go to the queue's end.
#
#This continues until none of the queue students want to take the top sandwich
#and are thus unable to eat.
#
#You are given two integer arrays students and sandwiches where sandwiches[i]
#is the type of the ith sandwich in the stack (i = 0 is the top) and
#students[j] is the preference of the jth student in the initial queue
#(j = 0 is the front of the queue).
#
#Return the number of students that are unable to eat.
#
#Example 1:
#Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
#Output: 0
#Explanation: Front student is 1, doesn't like 0, goes to back: [1,0,0,1], [0,1,0,1]
#Front student is 1, doesn't like 0, goes to back: [0,0,1,1], [0,1,0,1]
#Front student is 0, takes sandwich 0: [0,1,1], [1,0,1]
#... All students eat.
#
#Example 2:
#Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
#Output: 3
#
#Constraints:
#    1 <= students.length, sandwiches.length <= 100
#    students.length == sandwiches.length
#    sandwiches[i] is 0 or 1.
#    students[i] is 0 or 1.

from typing import List
from collections import Counter, deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Count preferences. Process sandwiches until one can't be taken.
        """
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                # No one wants this sandwich, remaining students can't eat
                break

        return count[0] + count[1]


class SolutionSimulation:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Direct simulation of the process.
        """
        queue = deque(students)
        stack = sandwiches[:]

        while queue and stack:
            rotations = 0

            while rotations < len(queue):
                if queue[0] == stack[0]:
                    queue.popleft()
                    stack.pop(0)
                    break
                else:
                    queue.append(queue.popleft())
                    rotations += 1
            else:
                # Made full rotation, no one wants top sandwich
                break

        return len(queue)


class SolutionArray:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Using array counts.
        """
        count = [0, 0]
        for s in students:
            count[s] += 1

        for s in sandwiches:
            if count[s] == 0:
                return count[0] + count[1]
            count[s] -= 1

        return 0


class SolutionCompact:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Compact solution.
        """
        c = Counter(students)
        for s in sandwiches:
            if c[s] == 0:
                return sum(c.values())
            c[s] -= 1
        return 0


class SolutionExplicit:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Explicit step-by-step simulation.
        """
        student_queue = list(students)
        sandwich_stack = list(sandwiches)

        unable = 0
        rounds_without_eating = 0

        while student_queue and sandwich_stack:
            if student_queue[0] == sandwich_stack[0]:
                # Student takes sandwich
                student_queue.pop(0)
                sandwich_stack.pop(0)
                rounds_without_eating = 0
            else:
                # Student goes to back
                student_queue.append(student_queue.pop(0))
                rounds_without_eating += 1

            # If we've gone through all students without anyone eating
            if rounds_without_eating == len(student_queue):
                break

        return len(student_queue)
