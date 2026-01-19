#239. Sliding Window Maximum
#Hard
#
#You are given an array of integers nums, there is a sliding window of size k which is moving
#from the very left of the array to the very right. You can only see the k numbers in the window.
#Each time the sliding window moves right by one position.
#
#Return the max sliding window.
#
#Example 1:
#Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#Output: [3,3,5,5,6,7]
#Explanation:
#Window position                Max
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
#
#Example 2:
#Input: nums = [1], k = 1
#Output: [1]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4
#    1 <= k <= nums.length

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for i in range(len(nums)):
            # Remove indices outside window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
