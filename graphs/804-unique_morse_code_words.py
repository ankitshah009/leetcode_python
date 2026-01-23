#804. Unique Morse Code Words
#Easy
#
#International Morse Code defines a standard encoding where each letter is
#mapped to a series of dots and dashes.
#
#Given an array of strings words where each word can be written as a
#concatenation of the Morse code of each letter.
#
#Return the number of different transformations among all words we have.
#
#Example 1:
#Input: words = ["gin","zen","gig","msg"]
#Output: 2
#Explanation: The transformation of each word is:
#"gin" -> "--...-."
#"zen" -> "--...-."
#"gig" -> "--...--."
#"msg" -> "--...--."
#There are 2 different transformations.
#
#Example 2:
#Input: words = ["a"]
#Output: 1
#
#Constraints:
#    1 <= words.length <= 100
#    1 <= words[i].length <= 12
#    words[i] consists of lowercase English letters.

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        """
        Convert each word to Morse and count unique codes.
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]

        def to_morse(word):
            return ''.join(morse[ord(c) - ord('a')] for c in word)

        return len(set(to_morse(word) for word in words))


class SolutionDict:
    """Using dictionary mapping"""

    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_map = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
            'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
            'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
            'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
            'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--",
            'z': "--.."
        }

        transformations = set()
        for word in words:
            code = ''.join(morse_map[c] for c in word)
            transformations.add(code)

        return len(transformations)


class SolutionCompact:
    """One-liner solution"""

    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
             "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
             "..-","...-",".--","-..-","-.--","--.."]
        return len({''.join(m[ord(c)-97] for c in w) for w in words})
