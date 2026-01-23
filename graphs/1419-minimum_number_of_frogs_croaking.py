#1419. Minimum Number of Frogs Croaking
#Medium
#
#You are given the string croakOfFrogs, which represents a combination of the
#string "croak" from different frogs, that is, multiple frogs can croak at the
#same time, so multiple "croak" are mixed.
#
#Return the minimum number of different frogs to finish all the croaks in the
#given string.
#
#A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', 'k'
#sequentially. The frogs have to print all five letters to finish a croak. If
#the given string is not a combination of a valid "croak" return -1.
#
#Example 1:
#Input: croakOfFrogs = "croakcroak"
#Output: 1
#Explanation: One frog yelling "croak" twice.
#
#Example 2:
#Input: croakOfFrogs = "crcoakroak"
#Output: 2
#Explanation: The minimum number of frogs is two.
#The first frog could yell "crcoakroak".
#The second frog could yell later "crcoakroak".
#
#Example 3:
#Input: croakOfFrogs = "croakcrook"
#Output: -1
#Explanation: The given string is an invalid combination of "croak" from
#different frogs.
#
#Constraints:
#    1 <= croakOfFrogs.length <= 10^5
#    croakOfFrogs is either 'c', 'r', 'o', 'a' or 'k'

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """
        Track how many frogs are at each stage of saying "croak".
        A frog at stage i can only move to stage i+1.
        """
        # Counts of frogs at each letter
        c = r = o = a = k = 0
        max_frogs = 0

        for char in croakOfFrogs:
            if char == 'c':
                c += 1
                max_frogs = max(max_frogs, c)
            elif char == 'r':
                if c > 0:
                    c -= 1
                    r += 1
                else:
                    return -1
            elif char == 'o':
                if r > 0:
                    r -= 1
                    o += 1
                else:
                    return -1
            elif char == 'a':
                if o > 0:
                    o -= 1
                    a += 1
                else:
                    return -1
            elif char == 'k':
                if a > 0:
                    a -= 1
                    k += 1
                else:
                    return -1

        # All frogs must have finished
        if c == r == o == a == 0:
            return max_frogs
        return -1


class SolutionArray:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """Using array for counts"""
        croak = "croak"
        char_to_idx = {c: i for i, c in enumerate(croak)}

        # counts[i] = frogs waiting after saying croak[i]
        counts = [0] * 5
        max_frogs = 0

        for char in croakOfFrogs:
            if char not in char_to_idx:
                return -1

            idx = char_to_idx[char]

            if idx == 0:
                # Starting new croak
                counts[0] += 1
                max_frogs = max(max_frogs, sum(counts[:4]) + 1)
            else:
                # Need a frog at previous stage
                if counts[idx - 1] > 0:
                    counts[idx - 1] -= 1
                    counts[idx] += 1
                else:
                    return -1

        # All frogs must have completed (only 'k' stage has counts)
        if all(counts[i] == 0 for i in range(4)):
            return max_frogs

        return -1


class SolutionSimplified:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """Simplified tracking"""
        cnt = [0] * 5
        char_idx = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        max_frogs = 0

        for ch in croakOfFrogs:
            i = char_idx[ch]
            cnt[i] += 1

            if i > 0 and cnt[i] > cnt[i - 1]:
                return -1

            if i == 0:
                max_frogs = max(max_frogs, cnt[0] - cnt[4])

        # Check all croaks completed
        return max_frogs if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] else -1
