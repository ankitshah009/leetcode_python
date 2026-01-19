#388. Longest Absolute File Path
#Medium
#
#Suppose we have a file system that stores both files and directories. An
#example of one system is represented in the following picture:
#
#dir
#    subdir1
#        file1.ext
#        subsubdir1
#    subdir2
#        subsubdir2
#            file2.ext
#
#We have the following string: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
#
#The directory dir contains an empty sub-directory subdir1 and a sub-directory
#subdir2 containing a file file2.ext.
#
#Return the length of the longest path to a file in the file system. If there
#is no file, return 0.
#
#Example 1:
#Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
#Output: 20
#Explanation: "dir/subdir2/file.ext" has length 20.
#
#Example 2:
#Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
#Output: 32
#Explanation: "dir/subdir2/subsubdir2/file2.ext" has length 32.
#
#Example 3:
#Input: input = "a"
#Output: 0
#Explanation: No file exists.
#
#Constraints:
#    1 <= input.length <= 10^4
#    input may contain lowercase or uppercase English letters, a new line
#    character '\n', a tab character '\t', a dot '.', a space ' ', and digits.

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        Use stack to track path lengths at each depth.
        """
        # Stack stores cumulative lengths at each depth
        # stack[i] = total length of path up to depth i
        stack = [0]  # Base: empty path has length 0
        max_length = 0

        for line in input.split('\n'):
            # Count tabs to determine depth
            depth = line.count('\t')
            name = line.lstrip('\t')

            # Pop until we're at parent level
            while len(stack) > depth + 1:
                stack.pop()

            # Current path length = parent length + / + name length
            current_length = stack[-1] + len(name) + 1  # +1 for '/'

            if '.' in name:
                # It's a file - update max (subtract 1 because no leading /)
                max_length = max(max_length, current_length - 1)
            else:
                # It's a directory - push to stack
                stack.append(current_length)

        return max_length


class SolutionDict:
    """Using dictionary to store depths"""

    def lengthLongestPath(self, input: str) -> int:
        # depth_lengths[d] = path length up to depth d
        depth_lengths = {-1: 0}
        max_length = 0

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')

            current_length = depth_lengths[depth - 1] + len(name) + 1

            if '.' in name:
                max_length = max(max_length, current_length - 1)
            else:
                depth_lengths[depth] = current_length

        return max_length


class SolutionArray:
    """Using array for depths"""

    def lengthLongestPath(self, input: str) -> int:
        # lengths[i] = cumulative length at depth i
        lengths = [0] * (input.count('\t') + 2)
        max_length = 0

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')

            lengths[depth + 1] = lengths[depth] + len(name) + 1

            if '.' in name:
                max_length = max(max_length, lengths[depth + 1] - 1)

        return max_length
