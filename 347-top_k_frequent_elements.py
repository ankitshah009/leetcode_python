#347. Top K Frequent Elements
#Medium
#
#Given an integer array nums and an integer k, return the k most frequent elements.
#You may return the answer in any order.
#
#Example 1:
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
#
#Example 2:
#Input: nums = [1], k = 1
#Output: [1]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4
#    k is in the range [1, the number of unique elements in the array].
#    It is guaranteed that the answer is unique.

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort approach - O(n)
        count = Counter(nums)
        n = len(nums)

        # Create buckets where index is frequency
        buckets = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Collect k most frequent
        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        # Heap approach - O(n log k)
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
