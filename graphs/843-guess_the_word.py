#843. Guess the Word
#Hard
#
#This is an interactive problem.
#
#You are given an array of unique strings words where words[i] is six letters long.
#One word in words was chosen as a secret word.
#
#You are also given the helper object Master. You may call Master.guess(word)
#where word is a six-letter-long string, and it must be from words. Master.guess
#returns:
#- -1 if word is not from words, or
#- an integer representing the number of exact matches (value and position) of
#  your guess to the secret word.
#
#There is a parameter allowedGuesses for each test case where allowedGuesses is
#the maximum number of times you can call Master.guess.
#
#For each test case, you should call Master.guess with the secret word without
#exceeding the maximum number of allowed guesses. You will get:
#- "Either you took too many guesses, or you did not find the secret word." if
#  you exceed allowedGuesses or called Master.guess with a word not in words
#- "You guessed the secret word correctly." if you called Master.guess with the
#  secret word within allowedGuesses
#
#Example 1:
#Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
#Output: You guessed the secret word correctly.
#
#Example 2:
#Input: secret = "hameli", words = ["hameli","abcdef"], allowedGuesses = 10
#Output: You guessed the secret word correctly.
#
#Constraints:
#    1 <= words.length <= 100
#    words[i].length == 6
#    words[i] consist of lowercase English letters.
#    All the strings of words are unique.
#    secret exists in words.
#    10 <= allowedGuesses <= 30

class Master:
    """Dummy Master class for type hints"""
    def guess(self, word: str) -> int:
        pass


class Solution:
    def findSecretWord(self, words: list[str], master: Master) -> None:
        """
        Minimax strategy: pick word that minimizes worst-case remaining candidates.
        After each guess, filter candidates based on match count.
        """
        def matches(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        def best_guess(candidates):
            """Find word that minimizes max group size after guessing"""
            if len(candidates) <= 2:
                return candidates[0]

            min_max_group = len(candidates)
            best = candidates[0]

            for word in candidates:
                # Count how many candidates would remain for each match count
                groups = [0] * 7
                for other in candidates:
                    groups[matches(word, other)] += 1

                # Max group size (excluding perfect match)
                max_group = max(groups[:6])
                if max_group < min_max_group:
                    min_max_group = max_group
                    best = word

            return best

        candidates = words[:]

        for _ in range(30):
            guess = best_guess(candidates)
            match_count = master.guess(guess)

            if match_count == 6:
                return

            # Filter candidates
            candidates = [w for w in candidates if matches(w, guess) == match_count]


class SolutionRandom:
    """Random selection with filtering"""

    def findSecretWord(self, words: list[str], master: Master) -> None:
        import random

        def matches(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        candidates = words[:]

        for _ in range(30):
            guess = random.choice(candidates)
            match_count = master.guess(guess)

            if match_count == 6:
                return

            candidates = [w for w in candidates if matches(w, guess) == match_count]


class SolutionMinZero:
    """Pick word with minimum zero-match count"""

    def findSecretWord(self, words: list[str], master: Master) -> None:
        def matches(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        candidates = words[:]

        for _ in range(30):
            # Pick word with minimum zero-matches with other words
            min_zeros = len(candidates)
            best = candidates[0]

            for word in candidates:
                zeros = sum(1 for other in candidates if matches(word, other) == 0)
                if zeros < min_zeros:
                    min_zeros = zeros
                    best = word

            match_count = master.guess(best)

            if match_count == 6:
                return

            candidates = [w for w in candidates if matches(w, best) == match_count]
