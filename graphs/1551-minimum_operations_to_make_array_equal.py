#1551. Minimum Operations to Make Array Equal
#Medium
#
#You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid
#values of i (i.e., 0 <= i < n).
#
#In one operation, you can select two indices x and y where 0 <= x, y < n and
#subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -= 1 and
#arr[y] += 1). The goal is to make all the elements of the array equal. It is
#guaranteed that all the elements of the array can be made equal using some
#operations.
#
#Given an integer n, the length of the array, return the minimum number of
#operations needed to make all the elements of arr equal.
#
#Example 1:
#Input: n = 3
#Output: 2
#Explanation: arr = [1, 3, 5]
#First operation: choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
#Second operation: choose x = 2 and y = 0, this leads arr to be [3, 3, 3]
#
#Example 2:
#Input: n = 6
#Output: 9
#
#Constraints:
#    1 <= n <= 10^4

class Solution:
    def minOperations(self, n: int) -> int:
        """
        Array is [1, 3, 5, ..., 2n-1]
        Target value is the mean = n (middle value)

        For each element below the mean, count how much needs to be added.
        Total operations = sum of (mean - arr[i]) for arr[i] < mean

        For odd n: elements are 1, 3, ..., n-2, n, n+2, ..., 2n-1
        For even n: elements are 1, 3, ..., n-1, n+1, ..., 2n-1

        Sum of differences from mean for first half:
        (n-1) + (n-3) + (n-5) + ... = sum of first n//2 even numbers for odd n
        """
        # Target is n (the middle value)
        # First half elements: 1, 3, 5, ..., 2*(n//2-1)+1 = 2*(n//2)-1
        # Differences: n-1, n-3, n-5, ...

        # For first n//2 elements, sum of (n - (2i+1)) for i in [0, n//2)
        # = sum of (n - 2i - 1) = n*k - 2*(0+1+...+(k-1)) - k where k = n//2
        # = nk - 2*k*(k-1)/2 - k = nk - k*(k-1) - k = k*(n - k + 1 - 1) = k*(n-k)

        k = n // 2
        return k * (n - k)


class SolutionSimplified:
    def minOperations(self, n: int) -> int:
        """
        Simplified formula.

        For n elements, we need to move first n//2 elements to the mean.
        If n is odd: sum = 2 + 4 + 6 + ... + (n-1) = n//2 * (n//2)
        If n is even: sum = 1 + 3 + 5 + ... + (n-1) = (n//2)^2
        """
        k = n // 2
        if n % 2 == 1:
            # Sum: 2 + 4 + ... + (n-1)
            # = 2 * (1 + 2 + ... + k) = 2 * k*(k+1)/2 = k*(k+1)
            # Wait, let me recalculate...
            # Elements: 1, 3, ..., n, ..., 2n-1
            # Target = n
            # Diffs for first k elements: (n-1), (n-3), ..., 2
            # = 2 + 4 + ... + (n-1) = k*k (since there are k terms)
            pass
        return k * k if n % 2 == 0 else k * (k + 1)


class SolutionDirect:
    def minOperations(self, n: int) -> int:
        """
        Direct calculation: sum differences from mean.
        """
        target = n  # Mean of arithmetic sequence 1, 3, ..., 2n-1
        total = 0

        for i in range(n // 2):
            element = 2 * i + 1
            total += target - element

        return total


class SolutionMath:
    def minOperations(self, n: int) -> int:
        """
        Mathematical derivation.

        arr[i] = 2i + 1, so arr = [1, 3, 5, ..., 2n-1]
        Sum = n^2, Mean = n

        For first half (i < n/2):
        diff[i] = n - (2i + 1) = n - 1 - 2i

        Sum of diffs for i in [0, n//2):
        = sum(n - 1 - 2i) for i = 0 to k-1, where k = n//2
        = k*(n-1) - 2*(0+1+...+(k-1))
        = k*(n-1) - k*(k-1)
        = k*(n - k)
        = (n//2) * (n - n//2)
        = (n//2) * ceil(n/2)
        """
        return (n // 2) * ((n + 1) // 2)


class SolutionOneLiner:
    def minOperations(self, n: int) -> int:
        """One-liner solution."""
        return n * n // 4
