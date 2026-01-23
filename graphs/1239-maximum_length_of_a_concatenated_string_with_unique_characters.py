#1239. Maximum Length of a Concatenated String with Unique Characters
#Medium
#
#You are given an array of strings arr. A string s is formed by the
#concatenation of a subsequence of arr that has unique characters.
#
#Return the maximum possible length of s.
#
#A subsequence is an array that can be derived from another array by deleting
#some or no elements without changing the order of the remaining elements.
#
#Example 1:
#Input: arr = ["un","iq","ue"]
#Output: 4
#Explanation: All the valid concatenations are:
#- ""
#- "un"
#- "iq"
#- "ue"
#- "uniq" ("un" + "iq")
#- "ique" ("iq" + "ue")
#Maximum length is 4.
#
#Example 2:
#Input: arr = ["cha","r","act","ers"]
#Output: 6
#Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers")
#and "acters" ("act" + "ers").
#
#Example 3:
#Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
#Output: 26
#Explanation: The only string in arr has all 26 characters.
#
#Constraints:
#    1 <= arr.length <= 16
#    1 <= arr[i].length <= 26
#    arr[i] contains only lowercase English letters.

from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        Backtracking with bitmask to track used characters.
        """
        def to_mask(s):
            """Convert string to bitmask, return -1 if has duplicates"""
            mask = 0
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if mask & bit:
                    return -1  # Duplicate character
                mask |= bit
            return mask

        # Convert all strings to masks, filter out invalid ones
        masks = []
        for s in arr:
            mask = to_mask(s)
            if mask != -1:
                masks.append((mask, len(s)))

        result = 0

        def backtrack(idx, current_mask, current_len):
            nonlocal result
            result = max(result, current_len)

            for i in range(idx, len(masks)):
                mask, length = masks[i]
                # Check if no overlap
                if current_mask & mask == 0:
                    backtrack(i + 1, current_mask | mask, current_len + length)

        backtrack(0, 0, 0)
        return result


class SolutionDP:
    def maxLength(self, arr: List[str]) -> int:
        """DP: Track all possible valid concatenations as bitmasks"""
        def to_mask(s):
            mask = 0
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if mask & bit:
                    return -1
                mask |= bit
            return mask

        # Start with empty concatenation
        dp = {0: 0}  # mask -> max length with this mask

        for s in arr:
            mask = to_mask(s)
            if mask == -1:
                continue

            # Try adding s to all existing concatenations
            new_dp = {}
            for existing_mask, existing_len in dp.items():
                if existing_mask & mask == 0:
                    new_mask = existing_mask | mask
                    new_len = existing_len + len(s)
                    if new_mask not in new_dp or new_dp[new_mask] < new_len:
                        new_dp[new_mask] = new_len

            # Merge into dp
            for m, l in new_dp.items():
                if m not in dp or dp[m] < l:
                    dp[m] = l

        return max(dp.values())


class SolutionSimple:
    def maxLength(self, arr: List[str]) -> int:
        """Simple recursive with set"""
        def backtrack(idx, current):
            if idx == len(arr):
                return len(current)

            result = backtrack(idx + 1, current)  # Skip current string

            # Try adding current string
            s = arr[idx]
            if len(set(s)) == len(s) and not (set(s) & current):
                result = max(result, backtrack(idx + 1, current | set(s)))

            return result

        return backtrack(0, set())
