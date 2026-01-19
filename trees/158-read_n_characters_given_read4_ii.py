#158. Read N Characters Given Read4 II - Call Multiple Times
#Hard
#
#Given a file and assume that you can only read the file using a given method
#read4, implement a method read to read n characters. Your method read may be
#called multiple times.
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
#Input: file = "abc", queries = [1, 2, 1]
#Output: [1, 2, 0]
#Explanation: read(1) returns 1 char "a", read(2) returns 2 chars "bc",
#read(1) returns 0 since file is exhausted.
#
#Example 2:
#Input: file = "abc", queries = [4, 1]
#Output: [3, 0]

# The read4 API is already defined for you.
def read4(buf4) -> int:
    pass

class Solution:
    def __init__(self):
        self.buffer = [''] * 4  # Internal buffer to store leftover characters
        self.buf_ptr = 0        # Pointer to current position in buffer
        self.buf_count = 0      # Number of characters in buffer

    def read(self, buf, n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total_read = 0

        while total_read < n:
            # If internal buffer is empty, read more from file
            if self.buf_ptr == self.buf_count:
                self.buf_count = read4(self.buffer)
                self.buf_ptr = 0

            # If no more characters available
            if self.buf_count == 0:
                break

            # Copy from internal buffer to destination
            while total_read < n and self.buf_ptr < self.buf_count:
                buf[total_read] = self.buffer[self.buf_ptr]
                total_read += 1
                self.buf_ptr += 1

        return total_read


class SolutionDeque:
    """Using deque for buffering"""

    def __init__(self):
        from collections import deque
        self.queue = deque()

    def read(self, buf, n: int) -> int:
        total_read = 0
        buf4 = [''] * 4

        while total_read < n:
            # First use buffered characters
            while self.queue and total_read < n:
                buf[total_read] = self.queue.popleft()
                total_read += 1

            if total_read == n:
                break

            # Read more from file
            count = read4(buf4)
            if count == 0:
                break

            # Add to buffer or directly to result
            for i in range(count):
                if total_read < n:
                    buf[total_read] = buf4[i]
                    total_read += 1
                else:
                    self.queue.append(buf4[i])

        return total_read
