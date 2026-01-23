#1630. Arithmetic Subarrays
#Medium
#
#A sequence of numbers is called arithmetic if it consists of at least two
#elements, and the difference between every two consecutive elements is the same.
#More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0]
#for all valid i.
#
#For example, these are arithmetic sequences:
#1, 3, 5, 7, 9
#7, 7, 7, 7
#3, -1, -5, -9
#
#The following sequence is not arithmetic:
#1, 1, 2, 5, 7
#
#You are given an array of n integers, nums, and two arrays of m integers each,
#l and r, representing the m range queries, where the ith query is the range
#[l[i], r[i]]. All the arrays are 0-indexed.
#
#Return a list of boolean elements answer, where answer[i] is true if the
#subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form
#an arithmetic sequence, and false otherwise.
#
#Example 1:
#Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
#Output: [true,false,true]
#Explanation:
#In the 0th query, [4,6,5] can be rearranged to [4,5,6] (arithmetic, diff=1).
#In the 1st query, [4,6,5,9] cannot form arithmetic sequence.
#In the 2nd query, [5,9,3,7] can be rearranged to [3,5,7,9] (arithmetic, diff=2).
#
#Example 2:
#Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
#Output: [false,true,false,false,true,true]
#
#Constraints:
#    n == nums.length
#    m == l.length
#    m == r.length
#    2 <= n <= 500
#    1 <= m <= 500
#    0 <= l[i] < r[i] < n
#    -10^5 <= nums[i] <= 10^5

from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        For each query, extract subarray, sort, check if arithmetic.
        """
        def is_arithmetic(arr: List[int]) -> bool:
            if len(arr) < 2:
                return False

            arr = sorted(arr)
            diff = arr[1] - arr[0]

            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False

            return True

        result = []
        for left, right in zip(l, r):
            subarray = nums[left:right + 1]
            result.append(is_arithmetic(subarray))

        return result


class SolutionNoSort:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        O(n) check without sorting: use set to verify arithmetic sequence.
        """
        def is_arithmetic(arr: List[int]) -> bool:
            n = len(arr)
            if n < 2:
                return False

            min_val = min(arr)
            max_val = max(arr)

            if min_val == max_val:
                return True  # All elements equal

            if (max_val - min_val) % (n - 1) != 0:
                return False

            diff = (max_val - min_val) // (n - 1)

            # Check all expected elements exist
            expected = set(min_val + i * diff for i in range(n))
            return set(arr) == expected

        return [is_arithmetic(nums[left:right + 1]) for left, right in zip(l, r)]


class SolutionDetailed:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        Detailed solution with explanation.
        """
        def check(subarray: List[int]) -> bool:
            """
            Check if array can be rearranged to arithmetic sequence.
            """
            n = len(subarray)
            if n <= 1:
                return True

            mn, mx = min(subarray), max(subarray)

            # All same values -> arithmetic with d=0
            if mn == mx:
                return True

            # Difference must divide evenly
            if (mx - mn) % (n - 1) != 0:
                return False

            d = (mx - mn) // (n - 1)

            # Every element should be min + k*d for some k in [0, n-1]
            seen = set()
            for num in subarray:
                # Check if (num - mn) is divisible by d
                if (num - mn) % d != 0:
                    return False
                k = (num - mn) // d
                if k < 0 or k >= n or k in seen:
                    return False
                seen.add(k)

            return len(seen) == n

        results = []
        m = len(l)

        for i in range(m):
            sub = nums[l[i]:r[i] + 1]
            results.append(check(sub))

        return results
