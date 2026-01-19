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

import heapq
from collections import Counter, deque

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        count = Counter(s)
        # Max heap: (-count, char)
        heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(heap)

        result = []
        cooldown = deque()  # (char, available_at_index)

        while heap or cooldown:
            # Add back characters whose cooldown is over
            if cooldown and cooldown[0][1] <= len(result):
                _, char = cooldown.popleft()
                heapq.heappush(heap, (-count[char], char))

            if not heap:
                return ""  # Can't place any character

            neg_cnt, char = heapq.heappop(heap)
            result.append(char)
            count[char] -= 1

            # Add to cooldown if more occurrences remain
            if count[char] > 0:
                cooldown.append((char, len(result) + k - 1))

        return ''.join(result)

    # Greedy with slots
    def rearrangeStringGreedy(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        count = Counter(s)
        # Max heap
        heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(heap)

        result = []

        while heap:
            # Take k most frequent characters
            temp = []

            for _ in range(min(k, len(s) - len(result))):
                if not heap:
                    return ""

                neg_cnt, char = heapq.heappop(heap)
                result.append(char)

                if -neg_cnt > 1:
                    temp.append((neg_cnt + 1, char))

            # Push back
            for item in temp:
                heapq.heappush(heap, item)

        return ''.join(result)
