#1570. Dot Product of Two Sparse Vectors
#Medium
#
#Given two sparse vectors, compute their dot product.
#
#Implement class SparseVector:
#- SparseVector(nums) Initializes the object with the vector nums
#- dotProduct(vec) Compute the dot product between the instance of SparseVector
#  and vec
#
#A sparse vector is a vector that has mostly zero values, you should store the
#sparse vector efficiently and compute the dot product between two SparseVector.
#
#Follow up: What if only one of the vectors is sparse?
#
#Example 1:
#Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
#Output: 8
#Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
#v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
#
#Example 2:
#Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
#Output: 0
#Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
#v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
#
#Example 3:
#Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
#Output: 6
#
#Constraints:
#    n == nums1.length == nums2.length
#    1 <= n <= 10^5
#    0 <= nums1[i], nums2[i] <= 100

from typing import List

class SparseVector:
    """
    Store only non-zero elements with their indices.
    """
    def __init__(self, nums: List[int]):
        # Store as dict: index -> value for non-zero elements
        self.data = {i: v for i, v in enumerate(nums) if v != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Iterate over smaller dict for efficiency
        if len(self.data) > len(vec.data):
            return vec.dotProduct(self)

        result = 0
        for idx, val in self.data.items():
            if idx in vec.data:
                result += val * vec.data[idx]

        return result


class SparseVectorList:
    """
    Store as list of (index, value) pairs.
    """
    def __init__(self, nums: List[int]):
        self.pairs = [(i, v) for i, v in enumerate(nums) if v != 0]

    def dotProduct(self, vec: 'SparseVectorList') -> int:
        # Two pointer approach since pairs are sorted by index
        result = 0
        i, j = 0, 0

        while i < len(self.pairs) and j < len(vec.pairs):
            if self.pairs[i][0] == vec.pairs[j][0]:
                result += self.pairs[i][1] * vec.pairs[j][1]
                i += 1
                j += 1
            elif self.pairs[i][0] < vec.pairs[j][0]:
                i += 1
            else:
                j += 1

        return result


class SparseVectorArray:
    """
    Store full array (for comparison, not memory efficient).
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def dotProduct(self, vec: 'SparseVectorArray') -> int:
        return sum(a * b for a, b in zip(self.nums, vec.nums))


class SparseVectorHybrid:
    """
    Hybrid approach: use dict if sparse, array if dense.
    """
    def __init__(self, nums: List[int]):
        non_zero = sum(1 for x in nums if x != 0)
        self.is_sparse = non_zero < len(nums) // 2

        if self.is_sparse:
            self.data = {i: v for i, v in enumerate(nums) if v != 0}
            self.nums = None
        else:
            self.data = None
            self.nums = nums

    def dotProduct(self, vec: 'SparseVectorHybrid') -> int:
        if self.is_sparse and vec.is_sparse:
            # Both sparse: iterate over smaller
            smaller = self.data if len(self.data) <= len(vec.data) else vec.data
            larger = vec.data if smaller is self.data else self.data
            return sum(v * larger.get(i, 0) for i, v in smaller.items())
        elif self.is_sparse:
            # Self sparse, vec dense
            return sum(v * vec.nums[i] for i, v in self.data.items())
        elif vec.is_sparse:
            # Self dense, vec sparse
            return sum(v * self.nums[i] for i, v in vec.data.items())
        else:
            # Both dense
            return sum(a * b for a, b in zip(self.nums, vec.nums))
