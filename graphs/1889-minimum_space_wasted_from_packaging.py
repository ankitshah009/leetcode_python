#1889. Minimum Space Wasted From Packaging
#Hard
#
#You have n packages that you are trying to place in boxes, one package in each
#box. There are m suppliers, and each supplier offers boxes of different sizes
#(with infinite supply). A package can be placed in a box if the size of the
#package is less than or equal to the size of the box.
#
#The package sizes are given as an integer array packages, where packages[i] is
#the size of the ith package. The suppliers are given as a 2D integer array
#boxes, where boxes[j] is an array of box sizes that the jth supplier offers.
#
#You want to choose a single supplier and use boxes from them such that the
#total wasted space is minimized. The wasted space of a package is the
#difference between the size of the box and the size of the package.
#
#Return the minimum total wasted space by choosing the box supplier optimally,
#or -1 if it is impossible to fit all the packages inside boxes.
#
#Example 1:
#Input: packages = [2,3,5], boxes = [[4,8],[2,8]]
#Output: 6
#
#Example 2:
#Input: packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]
#Output: -1
#
#Example 3:
#Input: packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]
#Output: 9
#
#Constraints:
#    n == packages.length
#    m == boxes.length
#    1 <= n <= 10^5
#    1 <= m <= 10^5
#    1 <= packages[i] <= 10^5
#    1 <= boxes[j].length <= 10^5
#    1 <= boxes[j][k] <= 10^5
#    sum(boxes[j].length) <= 10^5
#    The elements in boxes[j] are distinct.

from typing import List
import bisect

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        """
        For each supplier, binary search to assign packages to boxes.
        """
        MOD = 10**9 + 7

        packages.sort()
        n = len(packages)
        total_packages = sum(packages)

        # Prefix sum for fast range sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + packages[i]

        min_waste = float('inf')

        for supplier_boxes in boxes:
            supplier_boxes.sort()

            # Check if largest box can fit largest package
            if supplier_boxes[-1] < packages[-1]:
                continue

            waste = 0
            prev = 0  # Previous boundary index

            for box_size in supplier_boxes:
                # Find packages that fit in this box size
                # All packages[prev:idx] go into this box
                idx = bisect.bisect_right(packages, box_size)

                if idx > prev:
                    # Packages in range [prev, idx) use this box
                    count = idx - prev
                    package_sum = prefix[idx] - prefix[prev]
                    waste += box_size * count - package_sum
                    prev = idx

                if prev >= n:
                    break

            min_waste = min(min_waste, waste)

        return min_waste % MOD if min_waste != float('inf') else -1


class SolutionOptimized:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        """
        Same approach with cleaner implementation.
        """
        MOD = 10**9 + 7

        packages.sort()
        n = len(packages)
        max_package = packages[-1]

        # Prefix sums
        prefix = [0]
        for p in packages:
            prefix.append(prefix[-1] + p)

        min_waste = float('inf')

        for box_sizes in boxes:
            box_sizes.sort()

            # Skip if can't fit all packages
            if box_sizes[-1] < max_package:
                continue

            waste = 0
            left = 0

            for size in box_sizes:
                # Binary search for rightmost package <= size
                right = bisect.bisect_right(packages, size)

                if right > left:
                    # Waste for packages[left:right] using box of 'size'
                    package_sum = prefix[right] - prefix[left]
                    waste += size * (right - left) - package_sum

                left = right
                if left >= n:
                    break

            min_waste = min(min_waste, waste)

        return min_waste % MOD if min_waste < float('inf') else -1
