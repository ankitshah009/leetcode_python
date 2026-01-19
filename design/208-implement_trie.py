#208. Implement Trie (Prefix Tree)
#Medium
#
#Trie (we pronounce "try") or prefix tree is a tree data structure used to retrieve a key in a strings dataset. There are various applications of this very efficient data structure, such as autocomplete and spellchecker.
#
#Implement the Trie class:
#
#    Trie() initializes the trie object.
#    void insert(String word) inserts the string word to the trie.
#    boolean search(String word) returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#    boolean startsWith(String prefix) returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
# 
#
#Example 1:
#
#Input
#["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#Output
#[null, null, true, false, true, null, true]
#
#Explanation
#Trie trie = new Trie();
#trie.insert("apple");
#trie.search("apple");   // return True
#trie.search("app");     // return False
#trie.startsWith("app"); // return True
#trie.insert("app");
#trie.search("app");     // return True
#
# 
#
#Constraints:
#
#    1 <= word.length, prefix.length <= 2000
#    word and prefix consist of lowercase English letters.
#    At most 3 * 104 calls will be made to insert, search, and startsWith.
#
#

class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur=self.root
        for c in word:
            if c not in cur.children:
                # if character path does not exist, create it
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur=self.root
        for c in word:
            if c not in cur.children:
                # if character path does not exist, return False
                return False
            cur=cur.children[c]
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
