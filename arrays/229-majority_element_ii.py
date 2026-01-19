#229. Majority Element II
#Medium
#
#Given an integer array of size n, find all elements that appear more than ⌊n/3⌋ times.
#
#Example 1:
#Input: nums = [3,2,3]
#Output: [3]
#
#Example 2:
#Input: nums = [1]
#Output: [1]
#
#Example 3:
#Input: nums = [1,2]
#Output: [1,2]
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    -10^9 <= nums[i] <= 10^9
#
#Follow up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting Algorithm extended for n/3
        # There can be at most 2 elements with count > n/3

        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # First pass: find potential candidates
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Second pass: verify candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        result = []
        threshold = len(nums) // 3

        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return result

    # Hash map approach O(n) time, O(n) space
    def majorityElementHashMap(self, nums: List[int]) -> List[int]:
        from collections import Counter

        threshold = len(nums) // 3
        count = Counter(nums)

        return [num for num, freq in count.items() if freq > threshold]
