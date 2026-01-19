#211. Design Add and Search Words Data Structure
#Medium
#
#Design a data structure that supports adding new words and finding if a string
#matches any previously added string.
#
#Implement the WordDictionary class:
#    WordDictionary() Initializes the object.
#    void addWord(word) Adds word to the data structure.
#    bool search(word) Returns true if there is any string in the data structure
#    that matches word or false otherwise. word may contain dots '.' where dots
#    can be matched with any letter.
#
#Example:
#Input
#["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#Output
#[null,null,null,null,false,true,true,true]
#
#Constraints:
#    1 <= word.length <= 25
#    word in addWord consists of lowercase English letters.
#    word in search consists of '.' or lowercase English letters.
#    There will be at most 10^4 calls to addWord and search.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end

            char = word[index]

            if char == '.':
                # Try all possible children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)


class WordDictionaryIterative:
    """Iterative BFS approach for search"""

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        from collections import deque

        queue = deque([(self.root, 0)])

        while queue:
            node, index = queue.popleft()

            if index == len(word):
                if node.is_end:
                    return True
                continue

            char = word[index]

            if char == '.':
                for child in node.children.values():
                    queue.append((child, index + 1))
            elif char in node.children:
                queue.append((node.children[char], index + 1))

        return False


class WordDictionaryByLength:
    """Group words by length for faster wildcard search"""

    def __init__(self):
        from collections import defaultdict
        self.words_by_length = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.words_by_length[len(word)].add(word)

    def search(self, word: str) -> bool:
        import re
        pattern = re.compile('^' + word.replace('.', '.') + '$')

        for stored_word in self.words_by_length[len(word)]:
            if pattern.match(stored_word):
                return True

        return False
