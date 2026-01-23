#941. Valid Mountain Array
#Easy
#
#Given an array of integers arr, return true if and only if it is a valid
#mountain array.
#
#Recall that arr is a mountain array if and only if:
#- arr.length >= 3
#- There exists some i with 0 < i < arr.length - 1 such that:
#  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#Example 1:
#Input: arr = [2,1]
#Output: false
#
#Example 2:
#Input: arr = [3,5,5]
#Output: false
#
#Example 3:
#Input: arr = [0,3,2,1]
#Output: true
#
#Constraints:
#    1 <= arr.length <= 10^4
#    0 <= arr[i] <= 10^4

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        """
        Walk up from left, walk up from right, meet at peak.
        """
        n = len(arr)
        if n < 3:
            return False

        i = 0
        j = n - 1

        # Walk up from left
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Walk up from right
        while j > 0 and arr[j] < arr[j - 1]:
            j -= 1

        # Must meet in middle (not at edges)
        return i == j and 0 < i < n - 1


class SolutionOnePass:
    """One pass solution"""

    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Walk up
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # Walk down
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1


class SolutionState:
    """State machine approach"""

    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        state = 'up'  # 'up', 'down'
        went_up = False
        went_down = False

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                return False

            if arr[i] > arr[i - 1]:
                if state == 'down':
                    return False
                went_up = True
            else:
                if state == 'up':
                    state = 'down'
                went_down = True

        return went_up and went_down
