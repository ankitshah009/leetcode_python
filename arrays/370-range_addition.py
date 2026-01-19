#370. Range Addition
#Medium
#
#You are given an integer length and an array updates where updates[i] =
#[startIdxi, endIdxi, inci].
#
#You have an array arr of length length with all zeros, and you have some
#operation to apply on arr. In the ith operation, you should increment all the
#elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.
#
#Return arr after applying all the updates.
#
#Example 1:
#Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
#Output: [-2,0,3,5,3]
#
#Example 2:
#Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
#Output: [0,-4,2,2,2,4,4,-4,-4,-4]
#
#Constraints:
#    1 <= length <= 10^5
#    0 <= updates.length <= 10^4
#    0 <= startIdxi <= endIdxi < length
#    -1000 <= inci <= 1000

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Use difference array technique
        # Instead of updating range [start, end], we mark:
        # diff[start] += inc (range begins here)
        # diff[end + 1] -= inc (range ends after this)
        # Then compute prefix sum

        diff = [0] * (length + 1)

        for start, end, inc in updates:
            diff[start] += inc
            diff[end + 1] -= inc

        # Compute prefix sum
        result = [0] * length
        curr_sum = 0

        for i in range(length):
            curr_sum += diff[i]
            result[i] = curr_sum

        return result

    # In-place version
    def getModifiedArrayInPlace(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length

        for start, end, inc in updates:
            result[start] += inc
            if end + 1 < length:
                result[end + 1] -= inc

        # Compute prefix sum in place
        for i in range(1, length):
            result[i] += result[i - 1]

        return result
