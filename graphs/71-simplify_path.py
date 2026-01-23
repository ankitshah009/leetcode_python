#71. Simplify Path
#Medium
#
#Given an absolute path for a Unix-style file system, which begins with a slash
#'/', transform this path into its simplified canonical path.
#
#The rules are:
#- A single period '.' represents the current directory.
#- A double period '..' represents the previous/parent directory.
#- Multiple consecutive slashes '//' are treated as a single slash.
#- Any sequence of periods that does not match '.' or '..' is treated as a valid
#  directory or file name.
#
#The simplified canonical path should follow these rules:
#- It must start with a single slash '/'.
#- Directories are separated by a single slash '/'.
#- It must not end with a slash '/', unless it's the root directory.
#- It must not have any single or double periods representing current or parent
#  directories.
#
#Example 1:
#Input: path = "/home/"
#Output: "/home"
#
#Example 2:
#Input: path = "/home//foo/"
#Output: "/home/foo"
#
#Example 3:
#Input: path = "/home/user/Documents/../Pictures"
#Output: "/home/user/Pictures"
#
#Constraints:
#    1 <= path.length <= 3000
#    path consists of English letters, digits, '.', '/', or '_'.
#    path is a valid absolute Unix path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Stack-based approach.
        """
        stack = []

        for part in path.split('/'):
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)

        return '/' + '/'.join(stack)


class SolutionExplicit:
    def simplifyPath(self, path: str) -> str:
        """
        More explicit processing.
        """
        parts = path.split('/')
        stack = []

        for part in parts:
            if not part or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)


class SolutionDeque:
    def simplifyPath(self, path: str) -> str:
        """
        Using deque.
        """
        from collections import deque

        parts = path.split('/')
        dq = deque()

        for part in parts:
            if part == '..':
                if dq:
                    dq.pop()
            elif part and part != '.':
                dq.append(part)

        return '/' + '/'.join(dq)


class SolutionFilter:
    def simplifyPath(self, path: str) -> str:
        """
        Using filter with reduce.
        """
        from functools import reduce

        parts = filter(lambda x: x and x != '.', path.split('/'))

        def process(stack, part):
            if part == '..':
                return stack[:-1] if stack else stack
            return stack + [part]

        result = reduce(process, parts, [])
        return '/' + '/'.join(result)
