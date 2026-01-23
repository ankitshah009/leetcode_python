#1562. Find Latest Group of Size M
#Medium
#
#Given an array arr that represents a permutation of numbers from 1 to n.
#
#You have a binary string of size n that initially has all its bits set to zero.
#At each step i (assuming both the binary string and arr are 1-indexed) from 1
#to n, the bit at position arr[i] is set to 1.
#
#You are also given an integer m. Find the latest step at which there exists a
#group of ones of length m. A group of ones is a maximal contiguous substring of
#1's such that it cannot be extended in either direction.
#
#Return the latest step at which there exists a group of ones of length exactly m.
#If no such group exists, return -1.
#
#Example 1:
#Input: arr = [3,5,1,2,4], m = 1
#Output: 4
#Explanation:
#Step 1: "00100", groups: ["1"]
#Step 2: "00101", groups: ["1", "1"]
#Step 3: "10101", groups: ["1", "1", "1"]
#Step 4: "11101", groups: ["111", "1"]
#Step 5: "11111", groups: ["11111"]
#The latest step at which there exists a group of size 1 is step 4.
#
#Example 2:
#Input: arr = [3,1,5,4,2], m = 2
#Output: -1
#Explanation:
#Step 1: "00100", groups: ["1"]
#Step 2: "10100", groups: ["1", "1"]
#Step 3: "10101", groups: ["1", "1", "1"]
#Step 4: "10111", groups: ["1", "111"]
#Step 5: "11111", groups: ["11111"]
#No group of size 2 exists during any step.
#
#Example 3:
#Input: arr = [1], m = 1
#Output: 1
#
#Constraints:
#    n == arr.length
#    1 <= m <= n <= 10^5
#    1 <= arr[i] <= n
#    All integers in arr are distinct.

from typing import List

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        """
        Track group lengths and count of each length.

        For each bit set, merge with adjacent groups and update counts.
        """
        n = len(arr)
        if m == n:
            return n

        # length[i] = length of group containing position i
        # Only endpoints store the actual length
        length = [0] * (n + 2)  # Extra padding to avoid bounds checking

        # count[len] = number of groups with this length
        count = [0] * (n + 1)

        result = -1

        for step, pos in enumerate(arr, 1):
            left_len = length[pos - 1]
            right_len = length[pos + 1]

            new_len = left_len + right_len + 1

            # Update endpoints of the new merged group
            length[pos - left_len] = new_len
            length[pos + right_len] = new_len

            # Update counts
            count[left_len] -= 1
            count[right_len] -= 1
            count[new_len] += 1

            if count[m] > 0:
                result = step

        return result


class SolutionUnionFind:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        """
        Union-Find approach with size tracking.
        """
        n = len(arr)
        if m == n:
            return n

        parent = list(range(n + 1))
        size = [0] * (n + 1)
        count_m = 0
        result = -1

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count_m
            px, py = find(x), find(y)
            if px == py:
                return

            # Update count before merge
            if size[px] == m:
                count_m -= 1
            if size[py] == m:
                count_m -= 1

            # Merge smaller into larger
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]

            # Update count after merge
            if size[px] == m:
                count_m += 1

        bit_set = [False] * (n + 2)

        for step, pos in enumerate(arr, 1):
            bit_set[pos] = True
            size[pos] = 1

            # Check if new group of size m
            if 1 == m:
                count_m += 1

            # Merge with neighbors
            if bit_set[pos - 1]:
                union(pos, pos - 1)
            if bit_set[pos + 1]:
                union(pos, pos + 1)

            if count_m > 0:
                result = step

        return result


class SolutionSimulation:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        """
        Simulation with explicit group tracking (less efficient).
        """
        n = len(arr)
        bits = [0] * (n + 2)
        result = -1

        def count_groups_of_size_m():
            count = 0
            i = 1
            while i <= n:
                if bits[i] == 1:
                    j = i
                    while j <= n and bits[j] == 1:
                        j += 1
                    if j - i == m:
                        count += 1
                    i = j
                else:
                    i += 1
            return count

        for step, pos in enumerate(arr, 1):
            bits[pos] = 1

            # Check for groups of size m (inefficient)
            if count_groups_of_size_m() > 0:
                result = step

        return result


class SolutionReverse:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        """
        Process in reverse: Start with all 1s and remove bits.
        """
        n = len(arr)
        if m == n:
            return n

        length = [0] * (n + 2)
        count = {n: 1}  # Start with one group of size n

        # Process in reverse
        for step in range(n - 1, -1, -1):
            pos = arr[step]

            # Find current group boundaries
            left = pos
            while left > 0 and length[left - 1] == 0:
                left -= 1
            # This approach is tricky in reverse, use forward instead

        return -1  # Placeholder - forward approach is cleaner
