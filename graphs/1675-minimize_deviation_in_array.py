#1675. Minimize Deviation in Array
#Hard
#
#You are given an array nums of n positive integers.
#
#You can perform two types of operations on any element of the array any number
#of times:
#- If the element is even, divide it by 2.
#- If the element is odd, multiply it by 2.
#
#The deviation of the array is the maximum difference between any two elements
#in the array.
#
#Return the minimum deviation the array can have after performing some number
#of operations.
#
#Example 1:
#Input: nums = [1,2,3,4]
#Output: 1
#Explanation: Transform [1,2,3,4] to [1,2,3,2] or [2,2,3,4]. Deviation = 1.
#
#Example 2:
#Input: nums = [4,1,5,20,3]
#Output: 3
#Explanation: After [4,2,5,5,3], deviation = 5 - 2 = 3.
#
#Example 3:
#Input: nums = [2,10,8]
#Output: 3
#
#Constraints:
#    n == nums.length
#    2 <= n <= 5 * 10^4
#    1 <= nums[i] <= 10^9

from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        First, maximize all odd numbers (multiply by 2).
        Then, use max heap to repeatedly divide maximum until it's odd.
        Track minimum throughout.
        """
        # Convert all odds to even (their max value)
        max_heap = []
        min_val = float('inf')

        for num in nums:
            if num % 2 == 1:
                num *= 2
            heapq.heappush(max_heap, -num)
            min_val = min(min_val, num)

        min_deviation = -max_heap[0] - min_val

        # Keep reducing max until it becomes odd
        while max_heap[0] % 2 == 0:  # Note: negative, so check -max_heap[0]
            max_val = -heapq.heappop(max_heap)
            if max_val % 2 == 0:
                new_val = max_val // 2
                heapq.heappush(max_heap, -new_val)
                min_val = min(min_val, new_val)
                min_deviation = min(min_deviation, -max_heap[0] - min_val)
            else:
                heapq.heappush(max_heap, -max_val)
                break

        return min_deviation


class SolutionSortedSet:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        Using sorted set for efficient min/max tracking.
        """
        from sortedcontainers import SortedList

        # Convert all to max possible (odd * 2)
        processed = []
        for num in nums:
            if num % 2 == 1:
                num *= 2
            processed.append(num)

        sl = SortedList(processed)
        min_dev = sl[-1] - sl[0]

        # Reduce max while possible
        while sl[-1] % 2 == 0:
            max_val = sl.pop()
            sl.add(max_val // 2)
            min_dev = min(min_dev, sl[-1] - sl[0])

        return min_dev


class SolutionHeapAlt:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        Alternative heap approach.
        """
        # First make all numbers even (odd numbers get one *2)
        evens = []
        min_num = float('inf')

        for num in nums:
            if num % 2 == 1:
                num *= 2
            evens.append(-num)  # Max heap
            min_num = min(min_num, num)

        heapq.heapify(evens)
        result = -evens[0] - min_num

        while evens[0] % 2 == 0:
            curr_max = -heapq.heappop(evens)
            new_val = curr_max // 2
            min_num = min(min_num, new_val)
            heapq.heappush(evens, -new_val)
            result = min(result, -evens[0] - min_num)

        return result


class SolutionBFS:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        Explore all possible values for each number.
        Find minimum range that covers at least one value from each number.
        """
        # For each num, generate all possible values
        all_values = []
        for num in nums:
            values = set()
            if num % 2 == 1:
                num *= 2

            while num % 2 == 0:
                values.add(num)
                num //= 2
            values.add(num)
            all_values.append(values)

        # Merge intervals approach
        events = []
        for i, values in enumerate(all_values):
            for v in values:
                events.append((v, i))

        events.sort()

        # Sliding window to cover all indices
        from collections import defaultdict
        count = defaultdict(int)
        n = len(nums)
        covered = 0
        left = 0
        min_dev = float('inf')

        for right, (val, idx) in enumerate(events):
            if count[idx] == 0:
                covered += 1
            count[idx] += 1

            while covered == n:
                min_dev = min(min_dev, val - events[left][0])
                left_idx = events[left][1]
                count[left_idx] -= 1
                if count[left_idx] == 0:
                    covered -= 1
                left += 1

        return min_dev
