#670. Maximum Swap
#Medium
#
#You are given an integer num. You can swap two digits at most once to get the
#maximum valued number.
#
#Return the maximum valued number you can get.
#
#Example 1:
#Input: num = 2736
#Output: 7236
#Explanation: Swap the number 2 and the number 7.
#
#Example 2:
#Input: num = 9973
#Output: 9973
#Explanation: No swap.
#
#Constraints:
#    0 <= num <= 10^8

class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Track the rightmost occurrence of each digit.
        Find leftmost digit that can be improved by swapping with a larger digit to its right.
        """
        digits = list(str(num))
        n = len(digits)

        # last[d] = rightmost index where digit d appears
        last = {int(d): i for i, d in enumerate(digits)}

        # Find leftmost position where we can improve
        for i, d in enumerate(digits):
            # Check if there's a larger digit to the right
            for larger in range(9, int(d), -1):
                if last.get(larger, -1) > i:
                    # Swap
                    j = last[larger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))

        return num


class SolutionTwoPass:
    """Two-pass: find max suffix and swap point"""

    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)

        # max_right[i] = index of max digit from i to n-1
        max_right = [0] * n
        max_right[n - 1] = n - 1

        for i in range(n - 2, -1, -1):
            if digits[i] > digits[max_right[i + 1]]:
                max_right[i] = i
            else:
                max_right[i] = max_right[i + 1]

        # Find first position where swapping improves the number
        for i in range(n):
            j = max_right[i]
            if digits[j] > digits[i]:
                digits[i], digits[j] = digits[j], digits[i]
                break

        return int(''.join(digits))


class SolutionBruteForce:
    """Brute force: try all swaps"""

    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        max_num = num

        for i in range(n):
            for j in range(i + 1, n):
                digits[i], digits[j] = digits[j], digits[i]
                max_num = max(max_num, int(''.join(digits)))
                digits[i], digits[j] = digits[j], digits[i]

        return max_num
