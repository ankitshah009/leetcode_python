#358. Rearrange String k Distance Apart
#Hard
#
#Given a string s and an integer k, rearrange s such that the same characters
#are at least distance k from each other. If it is not possible to rearrange
#the string, return an empty string "".
#
#Example 1:
#Input: s = "aabbcc", k = 3
#Output: "abcabc"
#Explanation: The same letters are at least a distance of 3 from each other.
#
#Example 2:
#Input: s = "aaabc", k = 3
#Output: ""
#Explanation: It is not possible to rearrange the string.
#
#Example 3:
#Input: s = "aaadbbcc", k = 2
#Output: "abacabcd"
#Explanation: The same letters are at least a distance of 2 from each other.
#
#Constraints:
#    1 <= s.length <= 3 * 10^5
#    s consists of only lowercase English letters.
#    0 <= k <= s.length

from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """Greedy with max heap and cooldown queue"""
        if k <= 1:
            return s

        count = Counter(s)

        # Max heap: (-count, char)
        heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(heap)

        # Queue to track chars in cooldown: (release_time, count, char)
        cooldown = deque()
        result = []

        while heap or cooldown:
            # Release chars from cooldown if their time has come
            if cooldown and cooldown[0][0] <= len(result):
                _, cnt, char = cooldown.popleft()
                if cnt < 0:  # Still has remaining count
                    heapq.heappush(heap, (cnt, char))

            if not heap:
                if cooldown:
                    return ""  # Can't place any char but still have chars left
                break

            neg_cnt, char = heapq.heappop(heap)
            result.append(char)

            # Add to cooldown with updated count
            cooldown.append((len(result) + k - 1, neg_cnt + 1, char))

        return ''.join(result)


class SolutionSimple:
    """Simpler greedy approach"""

    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        count = Counter(s)
        heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(heap)

        result = []
        wait_queue = deque()

        while heap:
            neg_cnt, char = heapq.heappop(heap)
            result.append(char)

            # Add char to wait queue with remaining count
            wait_queue.append((char, neg_cnt + 1))

            # If queue reached k, we can reuse the front char
            if len(wait_queue) >= k:
                front_char, front_cnt = wait_queue.popleft()
                if front_cnt < 0:
                    heapq.heappush(heap, (front_cnt, front_char))

        return ''.join(result) if len(result) == len(s) else ""


class SolutionSlot:
    """Slot-based approach"""

    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        count = Counter(s)
        n = len(s)

        result = [''] * n
        sorted_chars = sorted(count.keys(), key=lambda x: -count[x])

        pos = 0
        for char in sorted_chars:
            for _ in range(count[char]):
                if pos >= n:
                    pos = (pos % k) + 1
                    if pos >= n:
                        return ""
                result[pos] = char
                pos += k

        return ''.join(result) if '' not in result else ""
