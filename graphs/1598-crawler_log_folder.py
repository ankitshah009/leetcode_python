#1598. Crawler Log Folder
#Easy
#
#The Leetcode file system keeps a log each time some user performs a change
#folder operation.
#
#The operations are described below:
#- "../" : Move to the parent folder of the current folder. (If you are already
#          in the main folder, remain in the same folder).
#- "./" : Remain in the same folder.
#- "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
#
#You are given a list of strings logs where logs[i] is the operation performed
#by the user at the ith step.
#
#The file system starts in the main folder, then the operations in logs are
#performed.
#
#Return the minimum number of operations needed to go back to the main folder
#after the change folder operations.
#
#Example 1:
#Input: logs = ["d1/","d2/","../","d21/","./"]
#Output: 2
#Explanation: Use "../" 2 times to go back to the main folder.
#
#Example 2:
#Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
#Output: 3
#
#Example 3:
#Input: logs = ["d1/","../","../","../"]
#Output: 0
#
#Constraints:
#    1 <= logs.length <= 10^3
#    2 <= logs[i].length <= 10
#    logs[i] contains lowercase English letters, digits, '.', and '/'.
#    logs[i] follows the format described above.
#    Folder names consist of lowercase letters and digits.

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        Track current depth from main folder.
        - "../" decreases depth (min 0)
        - "./" keeps same depth
        - "x/" increases depth
        """
        depth = 0

        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log == "./":
                pass  # Stay in same folder
            else:
                depth += 1

        return depth


class SolutionStack:
    def minOperations(self, logs: List[str]) -> int:
        """
        Stack-based approach: simulate folder structure.
        """
        stack = []  # Represents path from root

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log[:-1])  # Remove trailing '/'

        return len(stack)


class SolutionSimple:
    def minOperations(self, logs: List[str]) -> int:
        """
        Simple counter approach.
        """
        level = 0

        for operation in logs:
            if operation.startswith(".."):
                level = max(level - 1, 0)
            elif operation.startswith("."):
                continue
            else:
                level += 1

        return level


class SolutionMatch:
    def minOperations(self, logs: List[str]) -> int:
        """
        Using match-case (Python 3.10+).
        """
        depth = 0

        for log in logs:
            match log:
                case "../":
                    depth = max(0, depth - 1)
                case "./":
                    pass
                case _:
                    depth += 1

        return depth
