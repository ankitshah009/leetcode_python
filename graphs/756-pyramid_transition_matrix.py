#756. Pyramid Transition Matrix
#Medium
#
#You are stacking blocks to form a pyramid. Each block has a color, which is
#represented by a single letter. Each row of blocks contains one less block
#than the row beneath it and is centered on top.
#
#To make the pyramid aesthetically pleasing, there are only specific triangular
#patterns that are allowed. A triangular pattern consists of a single block
#stacked on top of two blocks. The patterns are given as a list of three-letter
#strings allowed, where the first two characters of a pattern represent the
#left and right bottom blocks respectively, and the third character is the top
#block.
#
#For example, "ABC" represents a triangular pattern with a 'C' block stacked on
#top of an 'A' (left) and 'B' (right) block. Note that this is different from
#"BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
#
#You are given a string bottom representing the bottom row of the pyramid, and
#a list of strings allowed representing the allowed triangular patterns.
#
#Return true if you can build the pyramid all the way to the top such that every
#triangular pattern in the pyramid is in allowed.
#
#Example 1:
#Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
#Output: true
#Explanation: The allowed triangular patterns are "BCC", "CDE", "CEA", and "FFF".
#Starting from the bottom (left to right), "BCC" produces "C", "CDE" produces "E".
#In the next level, "CE" produces "A".
#
#Example 2:
#Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
#Output: false
#
#Constraints:
#    2 <= bottom.length <= 6
#    0 <= allowed.length <= 216
#    allowed[i].length == 3

from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        """
        Build transition map, DFS to construct pyramid.
        """
        # Build transition map: (left, right) -> [possible tops]
        transitions = defaultdict(list)
        for pattern in allowed:
            transitions[(pattern[0], pattern[1])].append(pattern[2])

        def can_build(row):
            if len(row) == 1:
                return True

            # Try all possible next rows
            def build_next_row(idx, current):
                if idx == len(row) - 1:
                    return can_build(current)

                left, right = row[idx], row[idx + 1]
                for top in transitions[(left, right)]:
                    if build_next_row(idx + 1, current + top):
                        return True

                return False

            return build_next_row(0, "")

        return can_build(bottom)


class SolutionMemo:
    """With memoization"""

    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        from functools import lru_cache

        transitions = defaultdict(list)
        for pattern in allowed:
            transitions[(pattern[0], pattern[1])].append(pattern[2])

        @lru_cache(maxsize=None)
        def can_build(row):
            if len(row) == 1:
                return True

            # Generate all possible next rows
            def get_next_rows(idx):
                if idx == len(row) - 1:
                    return [""]

                left, right = row[idx], row[idx + 1]
                tops = transitions[(left, right)]
                if not tops:
                    return []

                result = []
                for top in tops:
                    for suffix in get_next_rows(idx + 1):
                        result.append(top + suffix)
                return result

            for next_row in get_next_rows(0):
                if can_build(next_row):
                    return True

            return False

        return can_build(bottom)


class SolutionIterative:
    """Iterative BFS approach"""

    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        from collections import deque

        transitions = defaultdict(list)
        for pattern in allowed:
            transitions[(pattern[0], pattern[1])].append(pattern[2])

        def get_all_next_rows(row):
            if len(row) == 1:
                return [row]

            result = [[]]
            for i in range(len(row) - 1):
                tops = transitions[(row[i], row[i + 1])]
                if not tops:
                    return []
                new_result = []
                for prefix in result:
                    for top in tops:
                        new_result.append(prefix + [top])
                result = new_result

            return [''.join(r) for r in result]

        queue = deque([bottom])
        visited = {bottom}

        while queue:
            row = queue.popleft()

            if len(row) == 1:
                return True

            for next_row in get_all_next_rows(row):
                if next_row not in visited:
                    visited.add(next_row)
                    queue.append(next_row)

        return False
