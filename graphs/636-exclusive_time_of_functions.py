#636. Exclusive Time of Functions
#Medium
#
#On a single-threaded CPU, we execute a program containing n functions. Each function
#has a unique ID between 0 and n-1.
#
#Function calls are stored in a call stack: when a function call starts, its ID is
#pushed onto the stack, and when a function call ends, its ID is popped off the stack.
#
#You are given a list logs, where logs[i] represents the ith log message formatted as
#"{function_id}:{"start" | "end"}:{timestamp}".
#
#Return the exclusive time of each function in an array, where the value at the ith
#index represents the exclusive time for the function with ID i.
#
#Example 1:
#Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
#Output: [3,4]
#
#Example 2:
#Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
#Output: [8]
#
#Constraints:
#    1 <= n <= 100
#    1 <= logs.length <= 500
#    0 <= function_id < n
#    0 <= timestamp <= 10^9
#    Two start events will not share the same timestamp.
#    Two end events will not share the same timestamp.
#    Each function has an "end" log for each "start" log.

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """Stack-based simulation"""
        result = [0] * n
        stack = []  # (function_id, start_time)
        prev_time = 0

        for log in logs:
            parts = log.split(':')
            func_id = int(parts[0])
            action = parts[1]
            timestamp = int(parts[2])

            if action == 'start':
                if stack:
                    # Add time to previous function
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:
                # End of current function
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return result


class SolutionVerbose:
    """More explicit handling"""

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []

        for log in logs:
            func_id, action, timestamp = log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)

            if action == 'start':
                if stack:
                    prev_func, prev_start = stack[-1]
                    result[prev_func] += timestamp - prev_start
                stack.append([func_id, timestamp])
            else:
                _, start_time = stack.pop()
                result[func_id] += timestamp - start_time + 1
                if stack:
                    stack[-1][1] = timestamp + 1

        return result
