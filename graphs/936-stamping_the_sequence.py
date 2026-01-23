#936. Stamping The Sequence
#Hard
#
#You are given two strings stamp and target. Initially, there is a string s of
#length target.length with all s[i] == '?'.
#
#In one turn, you can place stamp over s and replace every letter in s with the
#corresponding letter from stamp.
#
#Return an array of the index of the left-most letter being stamped at each turn.
#If we cannot obtain target from s within 10 * target.length turns, return [].
#
#Example 1:
#Input: stamp = "abc", target = "ababc"
#Output: [0,2]
#Explanation: [1,0,2] also valid.
#
#Example 2:
#Input: stamp = "abca", target = "aabcaca"
#Output: [3,0,1]
#
#Constraints:
#    1 <= stamp.length <= target.length <= 1000
#    stamp and target consist of lowercase English letters.

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        """
        Work backwards: repeatedly find stamp matches and replace with '?'.
        """
        m, n = len(stamp), len(target)
        target = list(target)
        result = []
        total_stamped = 0

        def can_stamp(pos: int) -> bool:
            """Check if stamp can be placed at position."""
            stamped = False
            for i in range(m):
                if target[pos + i] == '?':
                    continue
                if target[pos + i] != stamp[i]:
                    return False
                stamped = True
            return stamped

        def do_stamp(pos: int) -> int:
            """Stamp at position, return number of chars changed."""
            changed = 0
            for i in range(m):
                if target[pos + i] != '?':
                    target[pos + i] = '?'
                    changed += 1
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                if can_stamp(i):
                    count = do_stamp(i)
                    total_stamped += count
                    result.append(i)
                    changed = True

                    if total_stamped == n:
                        return result[::-1]

        return []


class SolutionBFS:
    """BFS approach with queue"""

    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        from collections import deque

        m, n = len(stamp), len(target)

        # For each position, track which stamp positions are matched
        # and which need to match
        queue = deque()
        done = [False] * (n - m + 1)
        result = []

        # For each target position, track windows containing it
        # and for each window, track matched/unmatched positions

        class Window:
            def __init__(self):
                self.matched = set()
                self.unmatched = set()

        windows = [Window() for _ in range(n - m + 1)]
        target_list = list(target)

        for i in range(n - m + 1):
            for j in range(m):
                if target_list[i + j] == stamp[j]:
                    windows[i].matched.add(j)
                else:
                    windows[i].unmatched.add(j)

            if not windows[i].unmatched:
                queue.append(i)
                done[i] = True

        total = 0
        while queue:
            pos = queue.popleft()
            result.append(pos)

            for j in range(m):
                idx = pos + j
                if target_list[idx] == '?':
                    continue

                total += 1
                target_list[idx] = '?'

                # Update all windows containing idx
                for k in range(max(0, idx - m + 1), min(n - m + 1, idx + 1)):
                    if done[k]:
                        continue
                    offset = idx - k
                    windows[k].unmatched.discard(offset)
                    if not windows[k].unmatched:
                        queue.append(k)
                        done[k] = True

        return result[::-1] if total == n else []
