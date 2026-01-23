#1646. Get Maximum in Generated Array
#Easy
#
#You are given an integer n. An array nums of length n + 1 is generated in the
#following way:
#- nums[0] = 0
#- nums[1] = 1
#- nums[2 * i] = nums[i] when 2 <= 2 * i <= n
#- nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
#
#Return the maximum integer in the array nums.
#
#Example 1:
#Input: n = 7
#Output: 3
#Explanation: According to the given rules:
#nums[0] = 0, nums[1] = 1
#nums[2] = nums[1] = 1, nums[3] = nums[1] + nums[2] = 2
#nums[4] = nums[2] = 1, nums[5] = nums[2] + nums[3] = 3
#nums[6] = nums[3] = 2, nums[7] = nums[3] + nums[4] = 3
#Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
#
#Example 2:
#Input: n = 2
#Output: 1
#
#Example 3:
#Input: n = 3
#Output: 2
#
#Constraints:
#    0 <= n <= 100

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Generate the array and find max.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        nums = [0] * (n + 1)
        nums[1] = 1

        for i in range(1, (n + 1) // 2 + 1):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]

        return max(nums)


class SolutionSimple:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Simpler generation loop.
        """
        if n < 2:
            return n

        nums = [0, 1] + [0] * (n - 1)

        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

        return max(nums)


class SolutionTrackMax:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Track max during generation.
        """
        if n == 0:
            return 0

        nums = [0] * (n + 1)
        nums[1] = 1
        max_val = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

            max_val = max(max_val, nums[i])

        return max_val


class SolutionCompact:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Compact solution.
        """
        if n < 2:
            return n

        a = [0, 1]
        for i in range(2, n + 1):
            a.append(a[i // 2] + (a[i // 2 + 1] if i % 2 else 0))

        return max(a)
