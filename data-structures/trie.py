class Node:
    def __init__(self):
        self.child = {}
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.isWord

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]
        return True

trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apricot")

print(trie.search("apple"))     # True
print(trie.search("app"))       # True
print(trie.search("apricot"))   # True
print(trie.search("ap"))        # False
print(trie.startsWith("ap"))    # True
