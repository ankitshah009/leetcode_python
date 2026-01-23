#1982. Find Array Given Subset Sums
#Hard
#
#You are given an integer n representing the length of an unknown array that
#you are trying to recover. You are also given an array sums containing the
#values of all 2^n subset sums of the unknown array (in no particular order).
#
#Return the array ans of length n representing the unknown array. If multiple
#answers exist, return any of them.
#
#An array sub is a subset of an array arr if sub can be obtained from arr by
#deleting some (possibly zero or all) elements of arr. The sum of the elements
#in sub is one possible subset sum of arr. The sum of an empty array is
#considered to be 0.
#
#Note: Test cases are generated such that there will always be at least one
#correct answer.
#
#Example 1:
#Input: n = 3, sums = [-3,-2,-1,0,0,1,2,3]
#Output: [1,2,-3]
#
#Example 2:
#Input: n = 2, sums = [0,0,0,0]
#Output: [0,0]
#
#Example 3:
#Input: n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
#Output: [0,-1,4,5]
#
#Constraints:
#    1 <= n <= 15
#    sums.length == 2^n
#    -10^4 <= sums[i] <= 10^4

from typing import List
from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        """
        Recursive approach: find one element, split sums, recurse.

        Key insight: difference between smallest and second smallest
        sum is either an element or negative of an element.
        """
        result = []
        sums.sort()

        for _ in range(n):
            # Potential element is difference between two smallest
            diff = sums[1] - sums[0]

            # Try splitting: sums with element vs sums without
            with_elem = Counter()
            without_elem = []
            has_zero_without = False

            temp_sums = Counter(sums)

            for s in sums:
                if temp_sums[s] > 0:
                    temp_sums[s] -= 1
                    temp_sums[s + diff] -= 1
                    without_elem.append(s)
                    if s == 0:
                        has_zero_without = True

            # Check if valid split (must contain 0 in one of the halves)
            if has_zero_without:
                result.append(diff)
                sums = without_elem
            else:
                result.append(-diff)
                sums = [s + diff for s in without_elem]

        return result


class SolutionIterative:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        """
        Iterative version with explicit splitting.
        """
        from collections import Counter

        sums.sort()
        result = []

        while len(sums) > 1:
            # Element candidate
            elem = sums[1] - sums[0]

            # Split sums into two groups
            count = Counter(sums)
            group1 = []  # Sums not including elem
            group2 = []  # Sums including elem

            for s in sums:
                if count[s] > 0:
                    count[s] -= 1
                    count[s + elem] -= 1
                    group1.append(s)
                    group2.append(s + elem)

            # Check which group contains 0
            if 0 in group1:
                result.append(elem)
                sums = group1
            else:
                result.append(-elem)
                sums = group2

        return result
