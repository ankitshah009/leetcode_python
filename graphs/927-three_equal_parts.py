#927. Three Equal Parts
#Hard
#
#You are given an array arr which consists of only zeros and ones, divide the
#array into three non-empty parts such that all of these parts represent the
#same binary value.
#
#If it is possible, return any [i, j] with i + 1 < j, such that:
#- arr[0], arr[1], ..., arr[i] is the first part,
#- arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
#- arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
#- All three parts have equal binary value.
#
#If it is not possible, return [-1, -1].
#
#Constraints:
#    3 <= arr.length <= 3 * 10^4
#    arr[i] is 0 or 1

class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        """
        Count 1s, divide equally. Match pattern from third part.
        """
        ones = sum(arr)

        # Edge case: all zeros
        if ones == 0:
            return [0, 2]

        # Must be divisible by 3
        if ones % 3 != 0:
            return [-1, -1]

        ones_per_part = ones // 3
        n = len(arr)

        # Find start positions of each part (first 1 of each part)
        count = 0
        first = second = third = -1

        for i, val in enumerate(arr):
            if val == 1:
                count += 1
                if count == 1:
                    first = i
                elif count == ones_per_part + 1:
                    second = i
                elif count == 2 * ones_per_part + 1:
                    third = i

        # Match pattern starting from each position
        while third < n:
            if arr[first] != arr[second] or arr[first] != arr[third]:
                return [-1, -1]
            first += 1
            second += 1
            third += 1

        # first-1 is end of part 1, second is start of part 3
        return [first - 1, second]


class SolutionExplicit:
    """More explicit pattern matching"""

    def threeEqualParts(self, arr: list[int]) -> list[int]:
        ones_idx = [i for i, x in enumerate(arr) if x == 1]

        if len(ones_idx) == 0:
            return [0, 2]

        if len(ones_idx) % 3 != 0:
            return [-1, -1]

        k = len(ones_idx) // 3
        n = len(arr)

        # Get pattern from third part
        start3 = ones_idx[2 * k]
        trailing_zeros = n - 1 - ones_idx[-1]

        # First part ends at ones_idx[k-1] + trailing_zeros
        end1 = ones_idx[k - 1] + trailing_zeros
        if end1 >= ones_idx[k]:
            return [-1, -1]

        # Second part ends at ones_idx[2*k-1] + trailing_zeros
        end2 = ones_idx[2 * k - 1] + trailing_zeros
        if end2 >= ones_idx[2 * k]:
            return [-1, -1]

        # Verify patterns match
        p1 = arr[ones_idx[0]:end1 + 1]
        p2 = arr[ones_idx[k]:end2 + 1]
        p3 = arr[ones_idx[2 * k]:n]

        if p1 == p2 == p3:
            return [end1, end2 + 1]

        return [-1, -1]
