#762. Prime Number of Set Bits in Binary Representation
#Easy
#
#Given two integers left and right, return the count of numbers in the inclusive
#range [left, right] having a prime number of set bits in their binary
#representation.
#
#Recall that the number of set bits an integer has is the number of 1's present
#when written in binary.
#
#Example 1:
#Input: left = 6, right = 10
#Output: 4
#Explanation:
#6 -> 110 (2 set bits, 2 is prime)
#7 -> 111 (3 set bits, 3 is prime)
#8 -> 1000 (1 set bit, 1 is not prime)
#9 -> 1001 (2 set bits, 2 is prime)
#10 -> 1010 (2 set bits, 2 is prime)
#4 numbers have a prime number of set bits.
#
#Example 2:
#Input: left = 10, right = 15
#Output: 5
#
#Constraints:
#    1 <= left <= right <= 10^6
#    0 <= right - left <= 10^4

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Count set bits, check if prime. Max bits for 10^6 is 20.
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        count = 0
        for num in range(left, right + 1):
            bits = bin(num).count('1')
            if bits in primes:
                count += 1

        return count


class SolutionPopcount:
    """Using bit_count method"""

    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(num.bit_count() in primes for num in range(left, right + 1))


class SolutionBitmask:
    """Using bitmask for prime check"""

    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Bitmask where bit i is set if i is prime
        # Primes up to 20: 2,3,5,7,11,13,17,19
        prime_mask = 0b10100010100010101100  # bits 2,3,5,7,11,13,17,19 are set

        count = 0
        for num in range(left, right + 1):
            bits = bin(num).count('1')
            if prime_mask & (1 << bits):
                count += 1

        return count
