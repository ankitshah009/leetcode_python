#140. Word Break II
#Hard
#
#Given a string s and a dictionary of strings wordDict, add spaces in s to construct a
#sentence where each word is a valid dictionary word. Return all such possible sentences
#in any order.
#
#Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#Example 1:
#Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
#Output: ["cats and dog","cat sand dog"]
#
#Example 2:
#Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
#Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
#
#Example 3:
#Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#Output: []
#
#Constraints:
#    1 <= s.length <= 20
#    1 <= wordDict.length <= 1000
#    1 <= wordDict[i].length <= 10
#    s and wordDict[i] consist of only lowercase English letters.
#    All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return backtrack(0)
