#1497. Check If Array Pairs Are Divisible by k
#Medium
#
#Given an array of integers arr of even length n and an integer k.
#
#We want to divide the array into exactly n / 2 pairs such that the sum of each
#pair is divisible by k.
#
#Return true If you can find a way to do that or false otherwise.
#
#Example 1:
#Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
#Output: true
#Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
#
#Example 2:
#Input: arr = [1,2,3,4,5,6], k = 7
#Output: true
#Explanation: Pairs are (1,6),(2,5) and (3,4).
#
#Example 3:
#Input: arr = [1,2,3,4,5,6], k = 10
#Output: false
#Explanation: You can try all possible pairs to see that there is no way to
#divide arr into 3 pairs each with sum divisible by 10.
#
#Constraints:
#    arr.length == n
#    1 <= n <= 10^5
#    n is even.
#    -10^9 <= arr[i] <= 10^9
#    1 <= k <= 10^5

from typing import List
from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        Count remainders mod k.
        For each remainder r, need count[r] == count[k-r].
        Special cases: r=0 needs even count, r=k/2 needs even count.
        """
        # Count remainders (handle negative numbers)
        remainder_count = Counter(x % k for x in arr)

        for r in remainder_count:
            if r == 0:
                # Elements with remainder 0 must pair with each other
                if remainder_count[r] % 2 != 0:
                    return False
            elif r * 2 == k:
                # If k is even, elements with remainder k/2 must pair together
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                # Count of remainder r must equal count of remainder k-r
                if remainder_count[r] != remainder_count.get(k - r, 0):
                    return False

        return True


class SolutionArray:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """Using array instead of Counter"""
        count = [0] * k

        for x in arr:
            count[x % k] += 1

        # Check remainder 0
        if count[0] % 2 != 0:
            return False

        # Check pairs
        for i in range(1, k // 2 + 1):
            if i == k - i:
                # Middle element when k is even
                if count[i] % 2 != 0:
                    return False
            else:
                if count[i] != count[k - i]:
                    return False

        return True


class SolutionOptimized:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        Optimized: only iterate through half of remainders.
        """
        count = [0] * k

        for x in arr:
            count[((x % k) + k) % k] += 1  # Handle negative numbers

        # Remainder 0 must have even count
        if count[0] % 2 != 0:
            return False

        # For each remainder r, check if count[r] == count[k-r]
        for r in range(1, (k + 1) // 2):
            if count[r] != count[k - r]:
                return False

        # If k is even, check middle
        if k % 2 == 0 and count[k // 2] % 2 != 0:
            return False

        return True


class SolutionGreedy:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """Greedy matching approach"""
        from collections import defaultdict

        remainder_count = defaultdict(int)

        for x in arr:
            r = x % k

            # Find complement
            complement = (k - r) % k

            if remainder_count[complement] > 0:
                remainder_count[complement] -= 1
            else:
                remainder_count[r] += 1

        # All counts should be 0 if perfect pairing exists
        return all(c == 0 for c in remainder_count.values())
