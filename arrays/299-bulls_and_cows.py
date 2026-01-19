#299. Bulls and Cows
#Medium
#
#You are playing the Bulls and Cows game with your friend.
#
#You write down a secret number and ask your friend to guess what the number is.
#When your friend makes a guess, you provide a hint with the following info:
#
#    The number of "bulls", which are digits in the guess that are in the correct
#    position.
#    The number of "cows", which are digits in the guess that are in your secret
#    number but are located in the wrong position.
#
#Given the secret number secret and your friend's guess guess, return the hint
#for your friend's guess.
#
#The hint should be formatted as "xAyB", where x is the number of bulls and y is
#the number of cows. Note that both secret and guess may contain duplicate digits.
#
#Example 1:
#Input: secret = "1807", guess = "7810"
#Output: "1A3B"
#Explanation: Bulls: 8. Cows: 1, 7, 0.
#
#Example 2:
#Input: secret = "1123", guess = "0111"
#Output: "1A1B"
#Explanation: Bulls: first 1. Cows: second or third 1.
#
#Constraints:
#    1 <= secret.length, guess.length <= 1000
#    secret.length == guess.length
#    secret and guess consist of digits only.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = [0] * 10
        guess_count = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[int(s)] += 1
                guess_count[int(g)] += 1

        # Cows: min count of each digit in both (excluding bulls)
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])

        return f"{bulls}A{cows}B"

    # One pass approach
    def getHintOnePass(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        counts = [0] * 10  # Positive: secret excess, Negative: guess excess

        for s, g in zip(secret, guess):
            s_digit, g_digit = int(s), int(g)

            if s == g:
                bulls += 1
            else:
                # Check if current secret digit was guessed before
                if counts[s_digit] < 0:
                    cows += 1
                counts[s_digit] += 1

                # Check if current guess digit was in secret before
                if counts[g_digit] > 0:
                    cows += 1
                counts[g_digit] -= 1

        return f"{bulls}A{cows}B"
