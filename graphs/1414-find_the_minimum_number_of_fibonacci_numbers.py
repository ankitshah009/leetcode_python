#1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
#Medium
#
#Given an integer k, return the minimum number of Fibonacci numbers whose sum
#is equal to k. The same Fibonacci number can be used multiple times.
#
#The Fibonacci numbers are defined as:
#    F1 = 1
#    F2 = 1
#    Fn = Fn-1 + Fn-2 for n > 2.
#
#It is guaranteed that for the given constraints we can always find such
#Fibonacci numbers that sum up to k.
#
#Example 1:
#Input: k = 7
#Output: 2
#Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
#For k = 7 we can use 2 + 5 = 7.
#
#Example 2:
#Input: k = 10
#Output: 2
#Explanation: For k = 10 we can use 2 + 8 = 10.
#
#Example 3:
#Input: k = 19
#Output: 3
#Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
#
#Constraints:
#    1 <= k <= 10^9

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """
        Greedy: Always pick the largest Fibonacci number <= remaining.
        This is optimal due to Zeckendorf's representation theorem.
        """
        # Generate Fibonacci numbers up to k
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])

        count = 0

        # Greedy from largest to smallest
        for i in range(len(fibs) - 1, -1, -1):
            if fibs[i] <= k:
                k -= fibs[i]
                count += 1

            if k == 0:
                break

        return count


class SolutionIterative:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """Iterative approach"""
        # Generate Fibonacci sequence
        fibs = []
        a, b = 1, 1
        while a <= k:
            fibs.append(a)
            a, b = b, a + b

        count = 0
        i = len(fibs) - 1

        while k > 0:
            if fibs[i] <= k:
                k -= fibs[i]
                count += 1
            i -= 1

        return count


class SolutionRecursive:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """Recursive approach"""
        if k == 0:
            return 0

        # Find largest Fibonacci number <= k
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b

        # a is now the largest Fib <= k
        return 1 + self.findMinFibonacciNumbers(k - a)


class SolutionBinarySearch:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """Using binary search to find largest Fib <= k"""
        import bisect

        # Generate Fibonacci numbers
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])

        count = 0
        while k > 0:
            # Find largest fib <= k
            idx = bisect.bisect_right(fibs, k) - 1
            k -= fibs[idx]
            count += 1

        return count
