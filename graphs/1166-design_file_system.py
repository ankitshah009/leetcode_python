#1166. Design File System
#Medium
#
#You are asked to design a file system that allows you to create new paths
#and associate them with different values.
#
#The format of a path is one or more concatenated strings of the form: /
#followed by one or more lowercase English letters. For example, "/leetcode"
#and "/leetcode/problems" are valid paths while an empty string "" and "/"
#are not.
#
#Implement the FileSystem class:
#    bool createPath(string path, int value) Creates a new path and associates
#    a value to it if possible and returns true. Returns false if the path
#    already exists or its parent path doesn't exist.
#    int get(string path) Returns the value associated with path or returns -1
#    if the path doesn't exist.
#
#Example 1:
#Input:
#["FileSystem","createPath","get"]
#[[],["/a",1],["/a"]]
#Output: [null,true,1]
#
#Example 2:
#Input:
#["FileSystem","createPath","createPath","get","createPath","get"]
#[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",3],["/c"]]
#Output: [null,true,true,2,false,-1]
#
#Constraints:
#    2 <= path.length <= 100
#    1 <= value <= 10^9
#    Each path is valid.
#    At most 10^4 calls will be made to createPath and get.

class FileSystem:
    """Simple hash map approach"""
    def __init__(self):
        self.paths = {"": -1}  # Root exists

    def createPath(self, path: str, value: int) -> bool:
        # Check if path already exists
        if path in self.paths:
            return False

        # Check if parent exists
        parent = path[:path.rfind('/')]
        if parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


class FileSystemTrie:
    """Trie-based approach for hierarchical structure"""
    def __init__(self):
        self.root = {}

    def createPath(self, path: str, value: int) -> bool:
        parts = path.split('/')[1:]  # Skip empty string before first /
        node = self.root

        # Navigate to parent
        for i in range(len(parts) - 1):
            if parts[i] not in node:
                return False  # Parent doesn't exist
            node = node[parts[i]]

        # Check if path already exists
        if parts[-1] in node:
            return False

        # Create new node
        node[parts[-1]] = {'_value': value}
        return True

    def get(self, path: str) -> int:
        parts = path.split('/')[1:]
        node = self.root

        for part in parts:
            if part not in node:
                return -1
            node = node[part]

        return node.get('_value', -1)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = -1


class FileSystemTrieNode:
    """Cleaner Trie with separate node class"""
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        parts = path.split('/')[1:]
        node = self.root

        for i, part in enumerate(parts):
            if part not in node.children:
                if i < len(parts) - 1:
                    return False  # Parent doesn't exist
                node.children[part] = TrieNode()
            elif i == len(parts) - 1:
                if node.children[part].value != -1:
                    return False  # Path exists
            node = node.children[part]

        node.value = value
        return True

    def get(self, path: str) -> int:
        parts = path.split('/')[1:]
        node = self.root

        for part in parts:
            if part not in node.children:
                return -1
            node = node.children[part]

        return node.value
