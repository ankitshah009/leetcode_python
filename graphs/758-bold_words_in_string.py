#758. Bold Words in String
#Medium
#
#Given an array of keywords words and a string s, make all appearances of all
#keywords words[i] in s bold. Any letters between <b> and </b> tags become bold.
#
#Return s after adding the bold tags. The returned string should use the least
#number of tags possible, and the tags should form a valid combination.
#
#Example 1:
#Input: words = ["ab","bc"], s = "aabcd"
#Output: "a<b>abc</b>d"
#Explanation: Note that returning "a<b>a<b>b</b>c</b>d" would use more tags,
#so it is incorrect.
#
#Example 2:
#Input: words = ["ab","cb"], s = "aabcd"
#Output: "a<b>ab</b>cd"
#
#Constraints:
#    1 <= s.length <= 500
#    0 <= words.length <= 50
#    1 <= words[i].length <= 10
#    s and words[i] consist of lowercase English letters.

class Solution:
    def boldWords(self, words: list[str], s: str) -> str:
        """
        Mark all positions that should be bold, then add tags.
        """
        n = len(s)
        bold = [False] * n

        # Mark all positions covered by any word
        for word in words:
            start = 0
            while True:
                idx = s.find(word, start)
                if idx == -1:
                    break
                for i in range(idx, idx + len(word)):
                    bold[i] = True
                start = idx + 1

        # Build result with merged tags
        result = []
        i = 0

        while i < n:
            if not bold[i]:
                result.append(s[i])
                i += 1
            else:
                result.append('<b>')
                while i < n and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append('</b>')

        return ''.join(result)


class SolutionIntervals:
    """Merge intervals approach"""

    def boldWords(self, words: list[str], s: str) -> str:
        n = len(s)
        intervals = []

        # Find all intervals to bold
        for word in words:
            start = 0
            while True:
                idx = s.find(word, start)
                if idx == -1:
                    break
                intervals.append([idx, idx + len(word)])
                start = idx + 1

        if not intervals:
            return s

        # Merge intervals
        intervals.sort()
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        # Build result
        result = []
        prev = 0

        for start, end in merged:
            result.append(s[prev:start])
            result.append('<b>')
            result.append(s[start:end])
            result.append('</b>')
            prev = end

        result.append(s[prev:])

        return ''.join(result)


class SolutionTrie:
    """Trie-based matching for efficiency"""

    def boldWords(self, words: list[str], s: str) -> str:
        # Build trie
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True

        n = len(s)
        bold = [False] * n

        # Match using trie
        for i in range(n):
            node = trie
            j = i
            while j < n and s[j] in node:
                node = node[s[j]]
                j += 1
                if '$' in node:
                    for k in range(i, j):
                        bold[k] = True

        # Build result
        result = []
        i = 0
        while i < n:
            if not bold[i]:
                result.append(s[i])
                i += 1
            else:
                result.append('<b>')
                while i < n and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append('</b>')

        return ''.join(result)
