#810. Chalkboard XOR Game
#Hard
#
#You are given an array of integers nums represents the numbers written on a
#chalkboard.
#
#Alice and Bob take turns erasing exactly one number from the chalkboard, with
#Alice starting first. If erasing a number causes the bitwise XOR of all the
#elements of the chalkboard to become 0, then that player loses. The bitwise
#XOR of one element is that element itself, and the bitwise XOR of no elements
#is 0.
#
#Also, if any player starts their turn with the bitwise XOR of all the elements
#of the chalkboard equal to 0, then that player wins.
#
#Return true if and only if Alice wins the game, assuming both players play
#optimally.
#
#Example 1:
#Input: nums = [1,1,2]
#Output: false
#Explanation: Alice has two choices: erase 1 or erase 2.
#If she erases 1, the nums array becomes [1, 2]. XOR = 3.
#If she erases 2, the nums array becomes [1, 1]. XOR = 0. Alice loses.
#Then Bob erases 1 or 2. Either way he wins.
#
#Example 2:
#Input: nums = [0,1]
#Output: true
#
#Example 3:
#Input: nums = [1,2,3]
#Output: true
#
#Constraints:
#    1 <= nums.length <= 1000
#    0 <= nums[i] < 2^16

class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        """
        Alice wins if:
        1. XOR of all elements is already 0, OR
        2. Number of elements is even (Alice can always make a safe move)

        Key insight: With even count and XOR != 0, at least two distinct
        numbers exist. Removing any number that keeps XOR != 0 is always possible.
        If all numbers are the same and XOR != 0, there must be odd count.
        """
        from functools import reduce
        from operator import xor

        total_xor = reduce(xor, nums)

        # Alice wins if XOR is 0 or count is even
        return total_xor == 0 or len(nums) % 2 == 0


class SolutionExplained:
    """With detailed explanation"""

    def xorGame(self, nums: list[int]) -> bool:
        """
        Game theory analysis:
        - If XOR = 0, current player wins immediately
        - If XOR != 0 and odd count, current player must make XOR = 0 eventually
        - If XOR != 0 and even count:
          - Not all elements can be equal (otherwise XOR = 0)
          - So there exists x where removing x doesn't make XOR = 0
          - After Alice's move: odd count for Bob
          - Bob faces the losing position
        """
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        return xor_sum == 0 or len(nums) % 2 == 0
