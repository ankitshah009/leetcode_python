#1859. Sorting the Sentence
#Easy
#
#A sentence is a list of words that are separated by a single space with no
#leading or trailing spaces. Each word consists of lowercase and uppercase
#English letters.
#
#A sentence can be shuffled by appending the 1-indexed word position to each
#word then rearranging the words in the sentence.
#
#For example, the sentence "This is a sentence" can be shuffled as
#"sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
#
#Given a shuffled sentence s containing no more than 9 words, reconstruct and
#return the original sentence.
#
#Example 1:
#Input: s = "is2 sentence4 This1 a3"
#Output: "This is a sentence"
#
#Example 2:
#Input: s = "Myself2 Me1 I4 and3"
#Output: "Me Myself and I"
#
#Constraints:
#    2 <= s.length <= 200
#    s consists of lowercase and uppercase English letters, spaces, and digits
#    from 1 to 9.
#    The number of words in s is between 1 and 9.
#    The words in s are separated by a single space.
#    s contains no leading or trailing spaces.

class Solution:
    def sortSentence(self, s: str) -> str:
        """
        Sort words by their position number.
        """
        words = s.split()
        # Sort by the last character (position number)
        words.sort(key=lambda w: w[-1])
        # Remove the position number from each word
        return ' '.join(w[:-1] for w in words)


class SolutionArray:
    def sortSentence(self, s: str) -> str:
        """
        Place words directly in correct positions.
        """
        words = s.split()
        result = [''] * len(words)

        for word in words:
            pos = int(word[-1]) - 1
            result[pos] = word[:-1]

        return ' '.join(result)


class SolutionDict:
    def sortSentence(self, s: str) -> str:
        """
        Using dictionary for position mapping.
        """
        words = s.split()
        position_map = {}

        for word in words:
            pos = int(word[-1])
            position_map[pos] = word[:-1]

        return ' '.join(position_map[i] for i in range(1, len(words) + 1))


class SolutionOneLiner:
    def sortSentence(self, s: str) -> str:
        """
        One-liner solution.
        """
        return ' '.join(w[:-1] for w in sorted(s.split(), key=lambda x: x[-1]))
