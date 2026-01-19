#912. Sort an Array
#Medium
#
#Given an array of integers nums, sort the array in ascending order and return it.
#
#You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
#and with the smallest space complexity possible.
#
#Example 1:
#Input: nums = [5,2,3,1]
#Output: [1,2,3,5]
#Explanation: After sorting the array, the positions of some numbers are not changed
#(for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
#
#Example 2:
#Input: nums = [5,1,1,2,0,0]
#Output: [0,0,1,1,2,5]
#Explanation: Note that the values of nums are not necessairly unique.
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    -5 * 10^4 <= nums[i] <= 5 * 10^4

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Quick sort implementation
        def quicksort(arr, low, high):
            if low < high:
                pivot = partition(arr, low, high)
                quicksort(arr, low, pivot - 1)
                quicksort(arr, pivot + 1, high)

        def partition(arr, low, high):
            # Use median of three for pivot selection
            mid = (low + high) // 2
            if arr[mid] < arr[low]:
                arr[low], arr[mid] = arr[mid], arr[low]
            if arr[high] < arr[low]:
                arr[low], arr[high] = arr[high], arr[low]
            if arr[mid] < arr[high]:
                arr[mid], arr[high] = arr[high], arr[mid]

            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        quicksort(nums, 0, len(nums) - 1)
        return nums
