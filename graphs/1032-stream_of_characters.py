#1032. Stream of Characters
#Hard
#
#Design an algorithm that accepts a stream of characters and checks if a
#suffix of these characters is a string of a given array of strings words.
#
#Implement the StreamChecker class:
#    StreamChecker(String[] words) Initializes the object with the strings
#        array words.
#    boolean query(char letter) Accepts a new character from the stream and
#        returns true if any non-empty suffix of the characters so far forms
#        one of the words in words.
#
#Example 1:
#Input
#["StreamChecker", "query", "query", "query", "query", "query", "query",
# "query", "query", "query", "query", "query", "query"]
#[[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"],
#  ["h"], ["i"], ["j"], ["k"], ["l"]]
#Output
#[null, false, false, false, true, false, true, false, false, false, false,
# false, true]
#
#Constraints:
#    1 <= words.length <= 2000
#    1 <= words[i].length <= 200
#    words[i] consists of lowercase English letters.
#    letter is a lowercase English letter.
#    At most 4 * 10^4 calls will be made to query.

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:
    """
    Build reverse trie from words.
    Store stream and check suffixes by traversing trie.
    """
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.stream = []
        self.max_len = 0

        # Insert reversed words into trie
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.root
            for c in reversed(word):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        # Check suffixes by traversing reversed trie
        node = self.root
        for i in range(len(self.stream) - 1, max(-1, len(self.stream) - 1 - self.max_len), -1):
            c = self.stream[i]
            if c not in node.children:
                return False
            node = node.children[c]
            if node.is_word:
                return True

        return False


class StreamCheckerAhoCorasick:
    """
    Aho-Corasick automaton for efficient multi-pattern matching.
    """
    def __init__(self, words: List[str]):
        from collections import deque

        self.goto = [{}]
        self.fail = [0]
        self.output = [False]
        self.state = 0

        # Build goto function
        for word in words:
            state = 0
            for c in word:
                if c not in self.goto[state]:
                    self.goto[state][c] = len(self.goto)
                    self.goto.append({})
                    self.fail.append(0)
                    self.output.append(False)
                state = self.goto[state][c]
            self.output[state] = True

        # Build fail function
        queue = deque()
        for c, s in self.goto[0].items():
            queue.append(s)

        while queue:
            r = queue.popleft()
            for c, s in self.goto[r].items():
                queue.append(s)
                state = self.fail[r]
                while state and c not in self.goto[state]:
                    state = self.fail[state]
                self.fail[s] = self.goto[state].get(c, 0)
                self.output[s] = self.output[s] or self.output[self.fail[s]]

    def query(self, letter: str) -> bool:
        while self.state and letter not in self.goto[self.state]:
            self.state = self.fail[self.state]
        self.state = self.goto[self.state].get(letter, 0)
        return self.output[self.state]
