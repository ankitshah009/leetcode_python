#809. Expressive Words
#Medium
#
#Sometimes people repeat letters to represent extra feeling. For example:
#"hello" -> "heeellooo" (i added 'e' and 'o')
#
#In these strings like "heeellooo", we have groups of adjacent letters that are
#all the same: "h", "eee", "ll", "ooo".
#
#You are given a string s and an array of query strings words. A query word is
#stretchy if it can be made to be equal to s by any number of applications of
#the following extension operation: choose a group of characters c, and add some
#number of characters c to the group so that the size of the group is three or more.
#
#For example, starting with "hello", we could do an extension on the group "o"
#to get "hellooo", but we cannot get "helloo" since the group "oo" has size less
#than 3. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
#
#Return the number of query strings that are stretchy.
#
#Example 1:
#Input: s = "heeellooo", words = ["hello", "hi", "helo"]
#Output: 1
#
#Example 2:
#Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
#Output: 3
#
#Constraints:
#    1 <= s.length, words.length <= 100
#    1 <= words[i].length <= 100
#    s and words[i] consist of lowercase letters.

class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        """
        Compress both strings into (char, count) pairs.
        Check if word can be stretched to match s.
        """
        def get_groups(string):
            """Return list of (char, count) tuples"""
            if not string:
                return []

            groups = []
            count = 1

            for i in range(1, len(string)):
                if string[i] == string[i - 1]:
                    count += 1
                else:
                    groups.append((string[i - 1], count))
                    count = 1

            groups.append((string[-1], count))
            return groups

        def is_stretchy(word):
            s_groups = get_groups(s)
            w_groups = get_groups(word)

            if len(s_groups) != len(w_groups):
                return False

            for (sc, s_cnt), (wc, w_cnt) in zip(s_groups, w_groups):
                if sc != wc:
                    return False

                # Check if valid extension
                if s_cnt < w_cnt:
                    return False

                if s_cnt != w_cnt and s_cnt < 3:
                    return False

            return True

        return sum(1 for word in words if is_stretchy(word))


class SolutionTwoPointer:
    """Two pointer approach"""

    def expressiveWords(self, s: str, words: list[str]) -> int:
        def is_stretchy(word):
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False

                # Count consecutive chars
                s_start = i
                while i < len(s) and s[i] == s[s_start]:
                    i += 1
                s_len = i - s_start

                w_start = j
                while j < len(word) and word[j] == word[w_start]:
                    j += 1
                w_len = j - w_start

                # Validate
                if s_len < w_len:
                    return False
                if s_len != w_len and s_len < 3:
                    return False

            return i == len(s) and j == len(word)

        return sum(1 for w in words if is_stretchy(w))


class SolutionGroupBy:
    """Using itertools.groupby"""

    def expressiveWords(self, s: str, words: list[str]) -> int:
        from itertools import groupby

        def groups(string):
            return [(c, len(list(g))) for c, g in groupby(string)]

        def check(word):
            sg = groups(s)
            wg = groups(word)

            if len(sg) != len(wg):
                return False

            for (sc, sn), (wc, wn) in zip(sg, wg):
                if sc != wc or sn < wn or (sn > wn and sn < 3):
                    return False

            return True

        return sum(check(w) for w in words)
