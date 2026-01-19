#71. Simplify Path
#Medium
#
#Given a string path, which is an absolute path (starting with a slash '/') to a file or
#directory in a Unix-style file system, convert it to the simplified canonical path.
#
#In a Unix-style file system, a period '.' refers to the current directory, a double period
#'..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//')
#are treated as a single slash '/'.
#
#The canonical path should have the following format:
#    The path starts with a single slash '/'.
#    Any two directories are separated by a single slash '/'.
#    The path does not end with a trailing '/'.
#    The path only contains the directories on the path from the root directory to the target
#    file or directory (i.e., no period '.' or double period '..')
#
#Return the simplified canonical path.
#
#Example 1:
#Input: path = "/home/"
#Output: "/home"
#
#Example 2:
#Input: path = "/../"
#Output: "/"
#
#Example 3:
#Input: path = "/home//foo/"
#Output: "/home/foo"
#
#Constraints:
#    1 <= path.length <= 3000
#    path consists of English letters, digits, period '.', slash '/' or '_'.
#    path is a valid absolute Unix path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)

        return '/' + '/'.join(stack)
