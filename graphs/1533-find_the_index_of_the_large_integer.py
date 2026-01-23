#1533. Find the Index of the Large Integer
#Medium
#
#We have an integer array arr, where all the integers in arr are equal except
#for one integer which is larger than the rest of the integers. You will not
#be given direct access to the array, instead, you will have an API ArrayReader
#which has the following functions:
#
#- int compareSub(int l, int r, int x, int y): where 0 <= l <= r < ArrayReader.length()
#  and 0 <= x <= y < ArrayReader.length(). Returns:
#  - 1 if the sum of subarray arr[l..r] is greater than the sum of subarray arr[x..y]
#  - 0 if the sum of subarray arr[l..r] is equal to the sum of subarray arr[x..y]
#  - -1 if the sum of subarray arr[l..r] is less than the sum of subarray arr[x..y]
#- int length(): Returns the size of the array.
#
#You are allowed to call compareSub() 20 times at most.
#
#Return the index of the largest element.
#
#Example 1:
#Input: arr = [7,7,7,7,10,7,7,7]
#Output: 4
#Explanation: The following calls to the API
#reader.compareSub(0, 0, 1, 1) // returns 0 this is a query comparing the sub-array (0, 0) with the sub array (1, 1), (i.e. compares arr[0] with arr[1]).
#reader.compareSub(2, 2, 3, 3) // returns 0
#reader.compareSub(4, 4, 5, 5) // returns 1, thus index 4 is the largest element.
#Notice that we made only 3 calls, so the answer is valid.
#
#Example 2:
#Input: arr = [6,6,12]
#Output: 2
#
#Constraints:
#    2 <= arr.length <= 5 * 10^5
#    1 <= arr[i] <= 100
#    All elements of arr are equal except for one element which is larger than all other elements.
#    At most 20 calls will be made to compareSub.

class ArrayReader:
    """Mock API class for testing"""
    def __init__(self, arr):
        self.arr = arr

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        sum1 = sum(self.arr[l:r+1])
        sum2 = sum(self.arr[x:y+1])
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        return 0

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        """
        Binary search: Compare two halves of the current range.
        The larger half contains the big element.
        If both halves have equal sum, the middle element (if any) is the answer.
        """
        left, right = 0, reader.length() - 1

        while left < right:
            mid = (left + right) // 2
            length = right - left + 1

            if length % 2 == 0:
                # Even length: compare [left, mid] with [mid+1, right]
                result = reader.compareSub(left, mid, mid + 1, right)
                if result == 1:
                    right = mid
                else:
                    left = mid + 1
            else:
                # Odd length: compare [left, mid-1] with [mid+1, right]
                if left == mid:
                    # Only 1 element
                    return left

                result = reader.compareSub(left, mid - 1, mid + 1, right)
                if result == 1:
                    right = mid - 1
                elif result == -1:
                    left = mid + 1
                else:
                    # Both equal, middle element is the answer
                    return mid

        return left


class SolutionAlternative:
    def getIndex(self, reader: 'ArrayReader') -> int:
        """
        Alternative: Always compare equal-sized subarrays.
        """
        left, right = 0, reader.length() - 1

        while left < right:
            length = right - left + 1
            half = length // 2

            # Compare first half with second half (excluding middle if odd)
            result = reader.compareSub(left, left + half - 1, right - half + 1, right)

            if result == 0:
                # Both halves equal, middle element is the large one
                return left + half
            elif result == 1:
                # Large element in first half
                right = left + half - 1
            else:
                # Large element in second half
                left = right - half + 1

        return left


class SolutionTernary:
    def getIndex(self, reader: 'ArrayReader') -> int:
        """
        Ternary search approach (less efficient but valid).
        """
        left, right = 0, reader.length() - 1

        while left < right:
            if right - left == 1:
                result = reader.compareSub(left, left, right, right)
                return left if result == 1 else right

            third = (right - left + 1) // 3

            # Compare first third with last third
            result = reader.compareSub(left, left + third - 1, right - third + 1, right)

            if result == 1:
                right = left + third - 1
            elif result == -1:
                left = right - third + 1
            else:
                # Large element in middle third
                left = left + third
                right = right - third

        return left
