#1860. Incremental Memory Leak
#Medium
#
#You are given two integers memory1 and memory2 representing the available
#memory in bits on two memory sticks. There is currently a faulty program
#running that consumes an increasing amount of memory every second.
#
#At the ith second (starting from 1), i bits of memory are allocated to the
#stick with more available memory (or from the first memory stick if both have
#the same available memory). If neither stick has at least i bits of available
#memory, the program crashes.
#
#Return an array containing [crashTime, memory1_crash, memory2_crash], where
#crashTime is the time (in seconds) when the program crashed and
#memory1_crash and memory2_crash are the available bits of memory in the first
#and second sticks respectively.
#
#Example 1:
#Input: memory1 = 2, memory2 = 2
#Output: [3,1,0]
#
#Example 2:
#Input: memory1 = 8, memory2 = 11
#Output: [6,0,4]
#
#Constraints:
#    0 <= memory1, memory2 <= 2^31 - 1

from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        """
        Simulate the process.
        """
        t = 1

        while memory1 >= t or memory2 >= t:
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t += 1

        return [t, memory1, memory2]


class SolutionMath:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        """
        Use math to skip when both memories are equal.

        When both equal, we alternate and consume 1+2+3+... from larger.
        But since we choose larger (or first if equal), this is still
        simulation-heavy. Math optimization is complex here.
        """
        # For competitive programming, simulation is fine given constraints
        # Sum of 1 to n is n*(n+1)/2, max sum is about 2^31 * 2 ≈ 2^32
        # sqrt(2^32) ≈ 65536 iterations max
        t = 1

        while memory1 >= t or memory2 >= t:
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t += 1

        return [t, memory1, memory2]


class SolutionBinarySearch:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        """
        Binary search to find crash time (complex due to allocation rules).
        Falls back to simulation for accuracy.
        """
        import math

        # Quick upper bound: total memory / average allocation
        total = memory1 + memory2
        # 1 + 2 + ... + t = t(t+1)/2 <= total
        # t <= sqrt(2*total)
        max_t = int(math.sqrt(2 * total)) + 2

        t = 1
        while t <= max_t and (memory1 >= t or memory2 >= t):
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t += 1

        return [t, memory1, memory2]
