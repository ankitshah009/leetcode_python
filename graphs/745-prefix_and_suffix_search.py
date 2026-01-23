#745. Prefix and Suffix Search
#Hard
#
#Design a special dictionary that searches the words in it by a prefix and a
#suffix.
#
#Implement the WordFilter class:
#- WordFilter(string[] words) Initializes the object with the words in the
#  dictionary.
#- f(string pref, string suff) Returns the index of the word in the dictionary,
#  which has the prefix pref and the suffix suff. If there is more than one
#  valid index, return the largest of them. If there is no such word in the
#  dictionary, return -1.
#
#Example 1:
#Input: ["WordFilter", "f"]
#       [[["apple"]], ["a", "e"]]
#Output: [null, 0]
#Explanation:
#WordFilter wordFilter = new WordFilter(["apple"]);
#wordFilter.f("a", "e"); // return 0, because word at index 0 has prefix "a"
#and suffix "e".
#
#Constraints:
#    1 <= words.length <= 10^4
#    1 <= words[i].length <= 7
#    1 <= pref.length, suff.length <= 7
#    words[i], pref and suff consist of lowercase English letters only.
#    At most 10^4 calls will be made to the function f.

class WordFilter:
    """
    Store all possible prefix#suffix combinations in a dictionary.
    """

    def __init__(self, words: list[str]):
        self.lookup = {}

        for idx, word in enumerate(words):
            n = len(word)
            # Generate all prefix#suffix combinations
            for i in range(n + 1):  # Prefixes
                for j in range(n + 1):  # Suffixes
                    key = word[:i] + '#' + word[j:]
                    self.lookup[key] = idx

    def f(self, pref: str, suff: str) -> int:
        key = pref + '#' + suff
        return self.lookup.get(key, -1)


class WordFilterTrie:
    """Trie-based approach with wrapped words"""

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.index = -1

    def __init__(self, words: list[str]):
        self.root = self.TrieNode()

        for idx, word in enumerate(words):
            # Insert all suffix#word combinations
            wrapped = word + '#' + word
            for i in range(len(word)):
                node = self.root
                for j in range(i, len(wrapped)):
                    c = wrapped[j]
                    if c not in node.children:
                        node.children[c] = self.TrieNode()
                    node = node.children[c]
                    node.index = idx

    def f(self, pref: str, suff: str) -> int:
        # Search for suff#pref in trie
        node = self.root
        search = suff + '#' + pref

        for c in search:
            if c not in node.children:
                return -1
            node = node.children[c]

        return node.index


class WordFilterDualTrie:
    """Separate prefix and suffix tries"""

    def __init__(self, words: list[str]):
        self.words = words
        self.prefix_map = {}
        self.suffix_map = {}

        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                prefix = word[:i]
                if prefix not in self.prefix_map:
                    self.prefix_map[prefix] = []
                self.prefix_map[prefix].append(idx)

                suffix = word[i:]
                if suffix not in self.suffix_map:
                    self.suffix_map[suffix] = []
                self.suffix_map[suffix].append(idx)

    def f(self, pref: str, suff: str) -> int:
        if pref not in self.prefix_map or suff not in self.suffix_map:
            return -1

        # Find intersection with highest index
        prefix_set = set(self.prefix_map[pref])
        suffix_indices = self.suffix_map[suff]

        for idx in reversed(suffix_indices):
            if idx in prefix_set:
                return idx

        return -1
