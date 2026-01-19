#384. Shuffle an Array
#Medium
#
#Given an integer array nums, design an algorithm to randomly shuffle the array.
#All permutations of the array should be equally likely as a result of the shuffling.
#
#Implement the Solution class:
#    Solution(int[] nums) Initializes the object with the integer array nums.
#    int[] reset() Resets the array to its original configuration and returns it.
#    int[] shuffle() Returns a random shuffling of the array.
#
#Example 1:
#Input: ["Solution", "shuffle", "reset", "shuffle"]
#       [[[1, 2, 3]], [], [], []]
#Output: [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
#Constraints:
#    1 <= nums.length <= 50
#    -10^6 <= nums[i] <= 10^6
#    All the elements of nums are unique.
#    At most 10^4 calls in total will be made to reset and shuffle.

import random

class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.array = nums

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        # Fisher-Yates shuffle
        n = len(self.array)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array
