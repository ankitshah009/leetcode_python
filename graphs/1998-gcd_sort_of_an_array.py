#1998. GCD Sort of an Array
#Hard
#
#You are given an integer array nums, and you can perform the following
#operation any number of times on nums:
#
#Swap the positions of two elements nums[i] and nums[j] if
#gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the greatest common
#divisor of nums[i] and nums[j].
#
#Return true if it is possible to sort nums in non-decreasing order using the
#above swap method, or false otherwise.
#
#Example 1:
#Input: nums = [7,21,3]
#Output: true
#Explanation: We can sort [7,21,3] in the following way:
#- Swap 7 and 21 (gcd(7,21) = 7 > 1). [21,7,3]
#- Swap 21 and 3 (gcd(21,3) = 3 > 1). [3,7,21]
#
#Example 2:
#Input: nums = [5,2,6,2]
#Output: false
#Explanation: Impossible to sort.
#
#Example 3:
#Input: nums = [10,5,9,3,15]
#Output: true
#Explanation: [10,5,9,3,15] -> [3,5,9,10,15]
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    2 <= nums[i] <= 10^5

from typing import List

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        """
        Union-Find: connect numbers sharing prime factors.
        Array is sortable if each element can reach its target position.
        """
        max_val = max(nums)

        # Union-Find with path compression
        parent = list(range(max_val + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            parent[find(x)] = find(y)

        # Sieve to find smallest prime factor
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Connect each number with its prime factors
        for num in nums:
            x = num
            while x > 1:
                prime = spf[x]
                union(num, prime)
                while x % prime == 0:
                    x //= prime

        # Check if sorted positions are reachable
        sorted_nums = sorted(nums)

        for i in range(len(nums)):
            if find(nums[i]) != find(sorted_nums[i]):
                return False

        return True


class SolutionFactorization:
    def gcdSort(self, nums: List[int]) -> bool:
        """
        Alternative factorization approach.
        """
        max_val = max(nums)
        parent = list(range(max_val + 1))

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        def union(x, y):
            parent[find(x)] = find(y)

        # Get prime factors
        def prime_factors(n):
            factors = []
            d = 2
            while d * d <= n:
                if n % d == 0:
                    factors.append(d)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1:
                factors.append(n)
            return factors

        # Union numbers with their prime factors
        for num in nums:
            for prime in prime_factors(num):
                union(num, prime)

        # Check sorting
        sorted_nums = sorted(nums)
        return all(find(nums[i]) == find(sorted_nums[i]) for i in range(len(nums)))


class SolutionOptimizedSieve:
    def gcdSort(self, nums: List[int]) -> bool:
        """
        Optimized with precomputed sieve.
        """
        max_val = max(nums)

        # Precompute smallest prime factors
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Union-Find
        parent = list(range(max_val + 1))
        rank = [0] * (max_val + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] < rank[py]:
                    px, py = py, px
                parent[py] = px
                if rank[px] == rank[py]:
                    rank[px] += 1

        # Connect with prime factors
        for num in nums:
            x = num
            while x > 1:
                p = spf[x]
                union(num, p)
                while x % p == 0:
                    x //= p

        # Verify sorting
        sorted_nums = sorted(nums)
        return all(find(a) == find(b) for a, b in zip(nums, sorted_nums))
