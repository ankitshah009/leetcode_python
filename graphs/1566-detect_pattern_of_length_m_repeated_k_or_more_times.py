#1566. Detect Pattern of Length M Repeated K or More Times
#Easy
#
#Given an array of positive integers arr, find a pattern of length m that is
#repeated k or more times.
#
#A pattern is a subarray (consecutive sub-sequence) that consists of one or more
#values, repeated multiple times consecutively without overlapping. A pattern is
#defined by its length and the number of repetitions.
#
#Return true if there exists a pattern of length m that is repeated k or more
#times, otherwise return false.
#
#Example 1:
#Input: arr = [1,2,4,4,4,4], m = 1, k = 3
#Output: true
#Explanation: The pattern (4) of length 1 is repeated 4 consecutive times.
#Notice that pattern can be repeated k or more times but not less.
#
#Example 2:
#Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
#Output: true
#Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times.
#Also, the pattern (1,1) is repeated 2 times.
#
#Example 3:
#Input: arr = [1,2,1,2,1,3], m = 2, k = 3
#Output: false
#Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times.
#There is no pattern of length 2 that is repeated 3 or more times.
#
#Example 4:
#Input: arr = [1,2,3,1,2], m = 2, k = 2
#Output: false
#Explanation: Notice that the pattern (1,2) exists twice but not consecutively.
#
#Constraints:
#    2 <= arr.length <= 100
#    1 <= arr[i] <= 100
#    1 <= m <= 100
#    2 <= k <= 100

from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Check if arr[i] == arr[i + m] for k*m - m consecutive positions.
        """
        n = len(arr)
        if m * k > n:
            return False

        count = 0
        for i in range(n - m):
            if arr[i] == arr[i + m]:
                count += 1
                if count >= m * (k - 1):
                    return True
            else:
                count = 0

        return False


class SolutionBruteForce:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Brute force: Check every possible starting position.
        """
        n = len(arr)

        for i in range(n - m * k + 1):
            # Check if pattern arr[i:i+m] repeats k times starting at i
            pattern = arr[i:i + m]
            valid = True

            for j in range(1, k):
                if arr[i + j * m:i + j * m + m] != pattern:
                    valid = False
                    break

            if valid:
                return True

        return False


class SolutionSlicing:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Using string matching / tuple matching.
        """
        n = len(arr)

        for i in range(n - m * k + 1):
            pattern = tuple(arr[i:i + m])

            match = True
            for rep in range(k):
                if tuple(arr[i + rep * m:i + rep * m + m]) != pattern:
                    match = False
                    break

            if match:
                return True

        return False


class SolutionStringConversion:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Convert to string and check for pattern repetition.
        """
        # Convert to string with separator
        s = ','.join(map(str, arr)) + ','
        n = len(arr)

        for i in range(n - m * k + 1):
            # Extract pattern as string
            pattern = ','.join(map(str, arr[i:i + m])) + ','

            # Check if pattern repeats k times
            repeated = pattern * k
            full = ','.join(map(str, arr[i:i + m * k])) + ','

            if full == repeated:
                return True

        return False


class SolutionOptimized:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Optimized: Count consecutive matching pairs at distance m.
        """
        n = len(arr)
        target = m * (k - 1)  # Need this many consecutive matches

        if target == 0:
            return True

        consecutive = 0

        for i in range(n - m):
            if arr[i] == arr[i + m]:
                consecutive += 1
                if consecutive >= target:
                    return True
            else:
                consecutive = 0

        return False
