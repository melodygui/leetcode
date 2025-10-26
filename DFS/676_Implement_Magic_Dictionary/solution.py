"""
Difficulty: medium 
Description:

  Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

  Implement the MagicDictionary class:

  MagicDictionary() Initializes the object.
  void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
  bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                # create node if character doesn't exist as a child
                currNode.children[char] = TrieNode()
            # move to child 
            currNode = currNode.children[char]
        
        # mark end of word for the last character 
        currNode.isEndOfWord = True

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        root = self.trie.root        
        
        def DFS(node: TrieNode, idx: int, used: bool) -> bool:  
            """
            Args:
                node: current node in the trie                 
                idx: current index in the word 
                used: if the one allowed char difference has been used 
            
            Returns:
                True if there is a word in the trie with only one character difference from the searchWord
            """      
            
            # base case: checked all characters in the search word 
            if idx == len(searchWord):
                return node.isEndOfWord and used                 
        
            searchChar = searchWord[idx]

            # first, if current character is one of the children, simply recurse on that child node
            if searchChar in node.children:
                if DFS(node.children[searchChar], idx + 1, used):
                    return True 
            
            # for the children chars that do not match, use the allowed one char diff and 
            return not used and any(
                DFS(node.children[char], idx + 1, True) 
                for char in node.children
                if char != searchChar)

        
        return DFS(root, 0, False)
        

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)