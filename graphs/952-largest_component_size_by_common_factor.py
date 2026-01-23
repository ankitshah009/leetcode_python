#952. Largest Component Size by Common Factor
#Hard
#
#You are given an integer array of unique positive integers nums. Consider the
#following graph:
#- There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
#- There is an edge between nums[i] and nums[j] if nums[i] and nums[j] share a
#  common factor greater than 1.
#
#Return the size of the largest connected component in the graph.
#
#Example 1:
#Input: nums = [4,6,15,35]
#Output: 4
#
#Example 2:
#Input: nums = [20,50,9,63]
#Output: 2
#
#Example 3:
#Input: nums = [2,3,6,7,4,12,21,39]
#Output: 8
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    1 <= nums[i] <= 10^5
#    All the values of nums are unique.

from collections import Counter

class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        """
        Union-Find by prime factors.
        """
        # Union-Find
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # For each number, union it with its prime factors
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

        for num in nums:
            factors = prime_factors(num)
            for f in factors:
                union(num, f)

        # Count component sizes (only for numbers in nums)
        return max(Counter(find(num) for num in nums).values())


class SolutionSieve:
    """Using sieve for faster factorization"""

    def largestComponentSize(self, nums: list[int]) -> int:
        max_val = max(nums)

        # Smallest prime factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        def get_prime_factors(n):
            factors = set()
            while n > 1:
                factors.add(spf[n])
                n //= spf[n]
            return factors

        for num in nums:
            for p in get_prime_factors(num):
                union(num, p)

        return max(Counter(find(num) for num in nums).values())
