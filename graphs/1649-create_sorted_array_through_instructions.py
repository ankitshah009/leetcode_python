#1649. Create Sorted Array through Instructions
#Hard
#
#Given an integer array instructions, you are asked to create a sorted array
#from the elements in instructions. You start with an empty container nums.
#For each element from left to right in instructions, insert it into nums.
#The cost of each insertion is the minimum of the following:
#- The number of elements currently in nums that are strictly less than
#  instructions[i].
#- The number of elements currently in nums that are strictly greater than
#  instructions[i].
#
#For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion
#is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3)
#and nums will become [1,2,3,3,5].
#
#Return the total cost to insert all elements from instructions into nums.
#Since the answer may be large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: instructions = [1,5,6,2]
#Output: 1
#Explanation: Insert 1 with cost min(0, 0) = 0, nums = [1].
#Insert 5 with cost min(1, 0) = 0, nums = [1,5].
#Insert 6 with cost min(2, 0) = 0, nums = [1,5,6].
#Insert 2 with cost min(1, 2) = 1, nums = [1,2,5,6].
#Total cost is 0 + 0 + 0 + 1 = 1.
#
#Example 2:
#Input: instructions = [1,2,3,6,5,4]
#Output: 3
#
#Example 3:
#Input: instructions = [1,3,3,3,2,4,2,1,2]
#Output: 4
#
#Constraints:
#    1 <= instructions.length <= 10^5
#    1 <= instructions[i] <= 10^5

from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        Binary Indexed Tree (Fenwick Tree) approach.
        Track count of each value, query prefix sums.
        """
        MOD = 10**9 + 7
        max_val = max(instructions) + 1

        # BIT for counting
        tree = [0] * (max_val + 1)

        def update(idx, delta=1):
            while idx <= max_val:
                tree[idx] += delta
                idx += idx & (-idx)

        def query(idx):
            """Sum of elements 1 to idx."""
            total = 0
            while idx > 0:
                total += tree[idx]
                idx -= idx & (-idx)
            return total

        total_cost = 0

        for i, num in enumerate(instructions):
            # Elements less than num
            less = query(num - 1)
            # Elements greater than num = total - less - equal
            # Total so far = i
            # Equal = query(num) - query(num-1)
            greater = i - query(num)

            cost = min(less, greater)
            total_cost = (total_cost + cost) % MOD

            update(num)

        return total_cost


class SolutionMergeSort:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        Merge sort based approach (counting inversions variant).
        """
        MOD = 10**9 + 7
        n = len(instructions)

        # Track smaller[i] = count of elements smaller than instructions[i] before i
        # Track larger[i] = count of elements larger than instructions[i] before i
        smaller = [0] * n
        larger = [0] * n

        def merge_count_smaller(indices):
            if len(indices) <= 1:
                return indices

            mid = len(indices) // 2
            left = merge_count_smaller(indices[:mid])
            right = merge_count_smaller(indices[mid:])

            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if instructions[left[i]] < instructions[right[j]]:
                    result.append(left[i])
                    i += 1
                else:
                    smaller[right[j]] += i
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                smaller[right[j]] += i
                result.append(right[j])
                j += 1

            return result

        def merge_count_larger(indices):
            if len(indices) <= 1:
                return indices

            mid = len(indices) // 2
            left = merge_count_larger(indices[:mid])
            right = merge_count_larger(indices[mid:])

            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if instructions[left[i]] > instructions[right[j]]:
                    result.append(left[i])
                    i += 1
                else:
                    larger[right[j]] += i
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                larger[right[j]] += i
                result.append(right[j])
                j += 1

            return result

        indices = list(range(n))
        merge_count_smaller(indices[:])
        merge_count_larger(list(range(n)))

        return sum(min(smaller[i], larger[i]) for i in range(n)) % MOD


class SolutionSegmentTree:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        Segment Tree approach for range queries.
        """
        MOD = 10**9 + 7
        max_val = max(instructions)

        # Segment tree size
        size = 1
        while size < max_val + 1:
            size *= 2

        tree = [0] * (2 * size)

        def update(idx):
            idx += size
            tree[idx] += 1
            while idx > 1:
                idx //= 2
                tree[idx] = tree[2 * idx] + tree[2 * idx + 1]

        def query(left, right):
            """Sum in range [left, right]."""
            left += size
            right += size + 1
            result = 0
            while left < right:
                if left & 1:
                    result += tree[left]
                    left += 1
                if right & 1:
                    right -= 1
                    result += tree[right]
                left //= 2
                right //= 2
            return result

        total = 0

        for i, num in enumerate(instructions):
            less = query(0, num - 1) if num > 0 else 0
            greater = query(num + 1, max_val) if num < max_val else 0

            total = (total + min(less, greater)) % MOD
            update(num)

        return total
