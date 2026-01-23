#1356. Sort Integers by The Number of 1 Bits
#Easy
#
#You are given an integer array arr. Sort the integers in the array in ascending
#order by the number of 1's in their binary representation and in case of two
#or more integers have the same number of 1's you have to sort them in ascending
#order.
#
#Return the array after sorting it.
#
#Example 1:
#Input: arr = [0,1,2,3,4,5,6,7,8]
#Output: [0,1,2,4,8,3,5,6,7]
#Explanation: [0] is the only integer with 0 bits.
#[1,2,4,8] all have 1 bit.
#[3,5,6] have 2 bits.
#[7] has 3 bits.
#The sorted array by bits is [0,1,2,4,8,3,5,6,7]
#
#Example 2:
#Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
#Output: [1,2,4,8,16,32,64,128,256,512,1024]
#Explanation: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
#
#Constraints:
#    1 <= arr.length <= 500
#    0 <= arr[i] <= 10^4

from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """Sort by (bit_count, value)"""
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


class SolutionPopcount:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """Using bit_count method (Python 3.10+) or manual popcount"""
        def popcount(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        return sorted(arr, key=lambda x: (popcount(x), x))


class SolutionBrianKernighan:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """Brian Kernighan's algorithm for bit counting"""
        def count_bits(n):
            count = 0
            while n:
                n &= n - 1  # Clear lowest set bit
                count += 1
            return count

        return sorted(arr, key=lambda x: (count_bits(x), x))
