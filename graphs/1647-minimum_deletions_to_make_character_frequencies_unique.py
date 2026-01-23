#1647. Minimum Deletions to Make Character Frequencies Unique
#Medium
#
#A string s is called good if there are no two different characters in s that
#have the same frequency.
#
#Given a string s, return the minimum number of characters you need to delete
#to make s good.
#
#The frequency of a character in a string is the number of times it appears in
#the string. For example, in the string "aab", the frequency of 'a' is 2, while
#the frequency of 'b' is 1.
#
#Example 1:
#Input: s = "aab"
#Output: 0
#Explanation: s is already good.
#
#Example 2:
#Input: s = "aaabbbcc"
#Output: 2
#Explanation: Delete two 'b's to get "aaabcc", or delete one 'b' and one 'c'.
#
#Example 3:
#Input: s = "ceabaacb"
#Output: 2
#Explanation: Delete both 'c's to get "eabaab".
#
#Constraints:
#    1 <= s.length <= 10^5
#    s contains only lowercase English letters.

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Count frequencies, then greedily reduce duplicates.
        Sort frequencies in descending order, ensure each is unique.
        """
        freq = Counter(s)
        frequencies = sorted(freq.values(), reverse=True)

        deletions = 0
        used = set()

        for f in frequencies:
            while f > 0 and f in used:
                f -= 1
                deletions += 1

            if f > 0:
                used.add(f)

        return deletions


class SolutionHeap:
    def minDeletions(self, s: str) -> int:
        """
        Using max-heap to process frequencies.
        """
        import heapq

        freq = Counter(s)
        # Max-heap (use negative values)
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)

        deletions = 0

        while len(heap) > 1:
            # Get largest frequency
            largest = -heapq.heappop(heap)

            # Check if duplicate with next largest
            if heap and -heap[0] == largest:
                # Must reduce this frequency
                if largest > 1:
                    heapq.heappush(heap, -(largest - 1))
                deletions += 1

        return deletions


class SolutionSort:
    def minDeletions(self, s: str) -> int:
        """
        Sort and process from largest.
        """
        freq = sorted(Counter(s).values(), reverse=True)

        deletions = 0
        max_allowed = len(s)  # Maximum possible frequency

        for f in freq:
            if f > max_allowed:
                deletions += f - max_allowed
                f = max_allowed

            max_allowed = max(0, f - 1)

        return deletions


class SolutionSet:
    def minDeletions(self, s: str) -> int:
        """
        Using set to track used frequencies.
        """
        freq = Counter(s)
        used = set()
        deletions = 0

        for char, count in freq.items():
            while count > 0 and count in used:
                count -= 1
                deletions += 1

            used.add(count)

        return deletions
