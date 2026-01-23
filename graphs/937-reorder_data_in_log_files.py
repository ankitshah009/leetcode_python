#937. Reorder Data in Log Files
#Medium
#
#You are given an array of logs. Each log is a space-delimited string of words,
#where the first word is the identifier.
#
#There are two types of logs:
#- Letter-logs: All words (except the identifier) consist of lowercase letters.
#- Digit-logs: All words (except the identifier) consist of digits.
#
#Reorder these logs so that:
#1. The letter-logs come before all digit-logs.
#2. The letter-logs are sorted lexicographically by their contents. If their
#   contents are the same, then sort them lexicographically by their identifiers.
#3. The digit-logs maintain their relative ordering.
#
#Return the final order of the logs.
#
#Example 1:
#Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig",
#               "let3 art zero"]
#Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1",
#         "dig2 3 6"]
#
#Constraints:
#    1 <= logs.length <= 100
#    3 <= logs[i].length <= 100
#    All the tokens of logs[i] are separated by a single space.
#    logs[i] is guaranteed to have an identifier and at least one word after it.

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        """
        Separate letter-logs and digit-logs, sort letter-logs.
        """
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, rest = log.split(' ', 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort letter-logs by (content, identifier)
        letter_logs.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))

        return letter_logs + digit_logs


class SolutionKey:
    """Using tuple key"""

    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def get_key(log):
            identifier, rest = log.split(' ', 1)

            if rest[0].isalpha():
                # Letter-log: sort by (0, content, identifier)
                return (0, rest, identifier)
            else:
                # Digit-log: sort by (1,) to maintain relative order
                return (1,)

        return sorted(logs, key=get_key)


class SolutionExplicit:
    """More explicit sorting"""

    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []

        for log in logs:
            parts = log.split()
            if parts[1][0].isdigit():
                digits.append(log)
            else:
                letters.append((parts[0], ' '.join(parts[1:]), log))

        # Sort letter-logs
        letters.sort(key=lambda x: (x[1], x[0]))

        return [x[2] for x in letters] + digits
