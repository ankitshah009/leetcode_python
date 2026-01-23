#989. Add to Array-Form of Integer
#Easy
#
#The array-form of an integer num is an array representing its digits in left
#to right order.
#
#Given num (the array-form of an integer) and an integer k, return the
#array-form of the integer num + k.
#
#Example 1:
#Input: num = [1,2,0,0], k = 34
#Output: [1,2,3,4]
#Explanation: 1200 + 34 = 1234
#
#Example 2:
#Input: num = [2,7,4], k = 181
#Output: [4,5,5]
#
#Example 3:
#Input: num = [2,1,5], k = 806
#Output: [1,0,2,1]
#
#Constraints:
#    1 <= num.length <= 10^4
#    0 <= num[i] <= 9
#    num does not contain any leading zeros except for 0 itself.
#    1 <= k <= 10^4

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        """
        Add digit by digit from right, carrying k.
        """
        result = []
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1

            result.append(k % 10)
            k //= 10

        return result[::-1]


class SolutionConvert:
    """Convert to int, add, convert back"""

    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        n = int(''.join(map(str, num))) + k
        return [int(d) for d in str(n)]


class SolutionCarry:
    """Explicit carry tracking"""

    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        # Convert k to array form
        k_arr = []
        while k > 0:
            k_arr.append(k % 10)
            k //= 10
        k_arr.reverse()

        # Pad shorter array
        n, m = len(num), len(k_arr)
        if n < m:
            num = [0] * (m - n) + num
        else:
            k_arr = [0] * (n - m) + k_arr

        # Add with carry
        result = []
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            total = num[i] + k_arr[i] + carry
            result.append(total % 10)
            carry = total // 10

        if carry:
            result.append(carry)

        return result[::-1]
