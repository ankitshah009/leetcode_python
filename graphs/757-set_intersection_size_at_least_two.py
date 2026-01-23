#757. Set Intersection Size At Least Two
#Hard
#
#You are given a 2D integer array intervals where intervals[i] = [starti, endi]
#represents all the integers from starti to endi inclusively.
#
#A containing set is an array nums where each interval from intervals has at
#least two integers in nums.
#
#Return the minimum possible size of a containing set.
#
#Example 1:
#Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
#Output: 3
#Explanation: Consider the set {2, 3, 4}. For each interval, there are at least
#2 numbers from the set in the interval.
#- [1, 3] has {2, 3} in the set.
#- [1, 4] has {2, 3, 4} in the set.
#- [2, 5] has {2, 3, 4} in the set.
#- [3, 5] has {3, 4} in the set.
#Note that {2, 3, 5} would also work as a containing set.
#
#Example 2:
#Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
#Output: 5
#Explanation: An example of a minimum sized set is {1, 2, 3, 4, 5}.
#
#Constraints:
#    1 <= intervals.length <= 3000
#    intervals[i].length == 2
#    0 <= starti < endi <= 10^8

class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        """
        Greedy: sort by end, then by start descending.
        For each interval, greedily pick numbers at the end.
        """
        # Sort by end point, then by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        result = []

        for start, end in intervals:
            # Count how many numbers from result are in [start, end]
            count = sum(1 for num in result if start <= num <= end)

            # Need at least 2 numbers
            while count < 2:
                # Add numbers from the end of interval
                if not result or result[-1] < end:
                    result.append(end)
                    end -= 1
                else:
                    # Find a number we haven't added yet
                    for num in range(end, start - 1, -1):
                        if num not in result[-3:]:  # Only check recent
                            result.append(num)
                            break
                count += 1

        return len(result)


class SolutionOptimized:
    """Optimized: track only last two numbers"""

    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        # Sort by end, then by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # Track last two numbers we've picked
        last1, last2 = -1, -1
        result = 0

        for start, end in intervals:
            # Count overlap with last two picked numbers
            overlap = 0
            if start <= last1:
                overlap += 1
            if start <= last2:
                overlap += 1

            if overlap == 0:
                # Need to pick two new numbers
                result += 2
                last2 = end - 1
                last1 = end
            elif overlap == 1:
                # Need one more number
                result += 1
                if start <= last1:
                    last2 = last1
                    last1 = end
                else:
                    last2 = end

            # If overlap == 2, we're good

        return result


class SolutionGreedy:
    """Cleaner greedy implementation"""

    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # Numbers we've selected (track just the last two that matter)
        selected = []
        total = 0

        for start, end in intervals:
            # Remove numbers outside current interval
            while selected and selected[0] < start:
                selected.pop(0)

            needed = 2 - len(selected)

            for i in range(needed):
                # Add from end, avoiding duplicates
                new_num = end - i
                while new_num in selected:
                    new_num -= 1
                selected.append(new_num)
                total += 1

            # Keep only last 2 (sorted)
            selected = sorted(selected)[-2:]

        return total
