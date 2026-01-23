#985. Sum of Even Numbers After Queries
#Medium
#
#You are given an integer array nums and an array queries where
#queries[i] = [vali, indexi].
#
#For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print
#the sum of the even values of nums.
#
#Return an integer array answer where answer[i] is the answer to the i-th query.
#
#Example 1:
#Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
#Output: [8,6,2,4]
#Explanation:
#After [1,0]: nums is [2,2,3,4], sum of evens = 8.
#After [-3,1]: nums is [2,-1,3,4], sum of evens = 6.
#After [-4,0]: nums is [-2,-1,3,4], sum of evens = 2.
#After [2,3]: nums is [-2,-1,3,6], sum of evens = 4.
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^4 <= nums[i] <= 10^4
#    1 <= queries.length <= 10^4
#    -10^4 <= vali <= 10^4
#    0 <= indexi < nums.length

class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Maintain running sum of evens.
        """
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []

        for val, idx in queries:
            # Remove old value if even
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            # Update value
            nums[idx] += val

            # Add new value if even
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            result.append(even_sum)

        return result


class SolutionExplicit:
    """More explicit cases"""

    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []

        for val, idx in queries:
            old = nums[idx]
            new = old + val

            was_even = old % 2 == 0
            is_even = new % 2 == 0

            if was_even and is_even:
                even_sum += val
            elif was_even and not is_even:
                even_sum -= old
            elif not was_even and is_even:
                even_sum += new
            # If was odd and still odd, no change

            nums[idx] = new
            result.append(even_sum)

        return result
