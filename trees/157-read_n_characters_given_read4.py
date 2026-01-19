#157. Read N Characters Given Read4
#Easy
#
#Given a file and assume that you can only read the file using a given method
#read4, implement a method to read n characters.
#
#Method read4:
#The API read4 reads four consecutive characters from file, then writes those
#characters into the buffer array buf4. The return value is the number of actual
#characters read.
#
#Method read:
#By using the read4 method, implement the method read that reads n characters
#from file and store it in the buffer array buf. Consider that you cannot
#manipulate file directly.
#
#Example 1:
#Input: file = "abc", n = 4
#Output: 3
#Explanation: After calling your read method, buf should contain "abc".
#
#Example 2:
#Input: file = "abcde", n = 5
#Output: 5
#Explanation: After calling your read method, buf should contain "abcde".
#
#Example 3:
#Input: file = "abcdABCD1234", n = 12
#Output: 12

# The read4 API is already defined for you.
def read4(buf4) -> int:
    pass

class Solution:
    def read(self, buf, n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total_read = 0
        buf4 = [''] * 4

        while total_read < n:
            # Read up to 4 characters
            count = read4(buf4)

            if count == 0:
                break  # End of file

            # Copy characters to destination buffer
            for i in range(min(count, n - total_read)):
                buf[total_read] = buf4[i]
                total_read += 1

        return total_read


class SolutionAlternative:
    """Alternative implementation using extend"""

    def read(self, buf, n: int) -> int:
        total_read = 0
        buf4 = [''] * 4
        eof = False

        while total_read < n and not eof:
            count = read4(buf4)

            if count < 4:
                eof = True

            # Calculate how many characters to actually use
            chars_to_use = min(count, n - total_read)

            for i in range(chars_to_use):
                buf[total_read + i] = buf4[i]

            total_read += chars_to_use

        return total_read
