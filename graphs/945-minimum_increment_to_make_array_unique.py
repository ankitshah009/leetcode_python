#945. Minimum Increment to Make Array Unique
#Medium
#
#You are given an integer array nums. In one move, you can pick an index i where
#0 <= i < nums.length and increment nums[i] by 1.
#
#Return the minimum number of moves to make every value in nums unique.
#
#The test cases are generated so that the answer fits in a 32-bit integer.
#
#Example 1:
#Input: nums = [1,2,2]
#Output: 1
#Explanation: Increment nums[2] to 3. Array becomes [1,2,3].
#
#Example 2:
#Input: nums = [3,2,1,2,1,7]
#Output: 6
#Explanation: After 6 moves, the array could be [3,4,1,2,5,7].
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^5

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """
        Sort and make each element at least prev + 1.
        """
        nums.sort()
        moves = 0
        need = 0  # Minimum value needed for current element

        for num in nums:
            need = max(need, num)
            moves += need - num
            need += 1

        return moves


class SolutionCounting:
    """Counting sort approach"""

    def minIncrementForUnique(self, nums: list[int]) -> int:
        max_val = max(nums) + len(nums)
        count = [0] * (max_val + 1)

        for num in nums:
            count[num] += 1

        moves = 0
        for i in range(len(count) - 1):
            if count[i] > 1:
                # Move duplicates to next position
                extra = count[i] - 1
                count[i + 1] += extra
                moves += extra

        return moves


class SolutionUnionFind:
    """Union-Find for next available slot"""

    def minIncrementForUnique(self, nums: list[int]) -> int:
        # root[x] = next available position >= x
        root = {}

        def find(x):
            if x not in root:
                root[x] = x
                return x
            root[x] = find(root[x] + 1)
            return root[x]

        moves = 0
        for num in nums:
            pos = find(num)
            moves += pos - num

        return moves
