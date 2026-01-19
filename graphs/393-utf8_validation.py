#393. UTF-8 Validation
#Medium
#
#Given an integer array data representing the data, return whether it is a
#valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded
#characters).
#
#A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
#rules:
#- For a 1-byte character, the first bit is a 0, followed by its Unicode code.
#- For an n-bytes character, the first n bits are all one's, the n + 1 bit is
#  0, followed by n - 1 bytes with the most significant 2 bits being 10.
#
#This is how the UTF-8 encoding would work:
#     Number of Bytes   |        UTF-8 Octet Sequence
#                       |              (binary)
#   --------------------+-----------------------------------------
#            1          |   0xxxxxxx
#            2          |   110xxxxx 10xxxxxx
#            3          |   1110xxxx 10xxxxxx 10xxxxxx
#            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#
#Example 1:
#Input: data = [197,130,1]
#Output: true
#Explanation: data represents the octet sequence: 11000101 10000010 00000001.
#It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte
#character.
#
#Example 2:
#Input: data = [235,140,4]
#Output: false
#
#Constraints:
#    1 <= data.length <= 2 * 10^4
#    0 <= data[i] <= 255

from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """Bit manipulation to check UTF-8 encoding"""
        # Number of continuation bytes expected
        continuation = 0

        for byte in data:
            if continuation > 0:
                # Expecting continuation byte: must start with 10
                if (byte >> 6) != 0b10:
                    return False
                continuation -= 1
            else:
                # Start of new character
                if (byte >> 7) == 0:
                    # 1-byte character: 0xxxxxxx
                    continuation = 0
                elif (byte >> 5) == 0b110:
                    # 2-byte character: 110xxxxx
                    continuation = 1
                elif (byte >> 4) == 0b1110:
                    # 3-byte character: 1110xxxx
                    continuation = 2
                elif (byte >> 3) == 0b11110:
                    # 4-byte character: 11110xxx
                    continuation = 3
                else:
                    # Invalid leading byte
                    return False

        return continuation == 0


class SolutionMasks:
    """Using explicit masks"""

    def validUtf8(self, data: List[int]) -> bool:
        MASK_1 = 0b10000000
        MASK_2 = 0b11100000
        MASK_3 = 0b11110000
        MASK_4 = 0b11111000
        MASK_CONT = 0b11000000

        remaining = 0

        for byte in data:
            if remaining > 0:
                if (byte & MASK_CONT) != 0b10000000:
                    return False
                remaining -= 1
            elif (byte & MASK_1) == 0:
                remaining = 0
            elif (byte & MASK_2) == 0b11000000:
                remaining = 1
            elif (byte & MASK_3) == 0b11100000:
                remaining = 2
            elif (byte & MASK_4) == 0b11110000:
                remaining = 3
            else:
                return False

        return remaining == 0


class SolutionBinary:
    """Using binary string representation"""

    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0

        for num in data:
            binary = format(num, '08b')

            if remaining > 0:
                if not binary.startswith('10'):
                    return False
                remaining -= 1
            else:
                if binary.startswith('0'):
                    remaining = 0
                elif binary.startswith('110'):
                    remaining = 1
                elif binary.startswith('1110'):
                    remaining = 2
                elif binary.startswith('11110'):
                    remaining = 3
                else:
                    return False

        return remaining == 0
