#1451. Rearrange Words in a Sentence
#Medium
#
#Given a sentence text (A sentence is a string of space-separated words) in the
#following format:
#    First letter is in upper case.
#    Each word in text are separated by a single space.
#
#Your task is to rearrange the words in text such that all words are rearranged
#in an increasing order of their lengths. If two words have the same length,
#arrange them in their original order.
#
#Return the new text following the format shown above.
#
#Example 1:
#Input: text = "Leetcode is cool"
#Output: "Is cool leetcode"
#Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and
#"cool" of length 4.
#Output is ordered by length and the new first word starts with uppercase.
#
#Example 2:
#Input: text = "Keep calm and code on"
#Output: "On and keep calm code"
#Explanation: Output is ordered as follows:
#"On" 2 letters.
#"and" 3 letters.
#"keep" 4 letters in case of tie order by position in original text.
#"calm" 4 letters.
#"code" 4 letters.
#
#Example 3:
#Input: text = "To be or not to be"
#Output: "To be or to be not"
#
#Constraints:
#    text begins with a capital letter and then contains lowercase letters and single space between words.
#    1 <= text.length <= 10^5

class Solution:
    def arrangeWords(self, text: str) -> str:
        """
        Split, sort by length (stable sort preserves original order for ties),
        then recapitalize first word.
        """
        words = text.lower().split()

        # Sort by length (Python's sort is stable)
        words.sort(key=len)

        # Capitalize first word
        words[0] = words[0].capitalize()

        return ' '.join(words)


class SolutionExplicit:
    def arrangeWords(self, text: str) -> str:
        """More explicit version"""
        # Convert to lowercase and split
        words = text.lower().split()

        # Sort by length, maintaining original order for same length
        sorted_words = sorted(enumerate(words), key=lambda x: (len(x[1]), x[0]))

        # Extract just the words
        result = [word for _, word in sorted_words]

        # Capitalize first letter
        result[0] = result[0][0].upper() + result[0][1:]

        return ' '.join(result)


class SolutionWithIndex:
    def arrangeWords(self, text: str) -> str:
        """Using index to track original order"""
        words = text.split()

        # Create list of (word, original_index)
        indexed_words = [(word.lower(), i) for i, word in enumerate(words)]

        # Sort by length, then by original index
        indexed_words.sort(key=lambda x: (len(x[0]), x[1]))

        # Build result
        result = [word for word, _ in indexed_words]

        # Capitalize first word
        result[0] = result[0].capitalize()

        return ' '.join(result)
