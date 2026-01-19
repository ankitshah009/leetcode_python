#315. Count of Smaller Numbers After Self
#Hard
#
#Given an integer array nums, return an integer array counts where counts[i] is
#the number of smaller elements to the right of nums[i].
#
#Example 1:
#Input: nums = [5,2,6,1]
#Output: [2,1,1,0]
#Explanation:
#To the right of 5 there are 2 smaller elements (2 and 1).
#To the right of 2 there is only 1 smaller element (1).
#To the right of 6 there is 1 smaller element (1).
#To the right of 1 there is 0 smaller element.
#
#Example 2:
#Input: nums = [-1]
#Output: [0]
#
#Example 3:
#Input: nums = [-1,-1]
#Output: [0,0]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """Merge sort with index tracking"""
        n = len(nums)
        counts = [0] * n

        # Array of (value, original_index)
        indexed = [(num, i) for i, num in enumerate(nums)]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            right_count = 0  # Count of right elements merged

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    # Left element is smaller or equal
                    counts[left[i][1]] += right_count
                    result.append(left[i])
                    i += 1
                else:
                    # Right element is smaller
                    right_count += 1
                    result.append(right[j])
                    j += 1

            # Remaining left elements
            while i < len(left):
                counts[left[i][1]] += right_count
                result.append(left[i])
                i += 1

            # Remaining right elements
            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        merge_sort(indexed)
        return counts


class SolutionBIT:
    """Binary Indexed Tree (Fenwick Tree)"""

    def countSmaller(self, nums: List[int]) -> List[int]:
        # Coordinate compression
        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}

        n = len(sorted_nums)
        tree = [0] * (n + 1)

        def update(i):
            while i <= n:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & (-i)
            return total

        counts = []

        # Process from right to left
        for num in reversed(nums):
            r = rank[num]
            # Count numbers with rank < r
            counts.append(query(r - 1))
            update(r)

        return counts[::-1]


class SolutionBST:
    """Using BST with count augmentation"""

    def countSmaller(self, nums: List[int]) -> List[int]:
        class BSTNode:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None
                self.left_count = 0  # Count of nodes in left subtree
                self.count = 1  # Count of this value

        def insert(root, val):
            smaller = 0
            while root:
                if val < root.val:
                    root.left_count += 1
                    if root.left:
                        root = root.left
                    else:
                        root.left = BSTNode(val)
                        break
                elif val > root.val:
                    smaller += root.left_count + root.count
                    if root.right:
                        root = root.right
                    else:
                        root.right = BSTNode(val)
                        break
                else:
                    smaller += root.left_count
                    root.count += 1
                    break
            return smaller

        if not nums:
            return []

        counts = [0] * len(nums)
        root = BSTNode(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            counts[i] = insert(root, nums[i])

        return counts
