R = 26 # Number of possible branches in tree (aka # of letters in alphabet)

class TrieNode:

    def __init__(self, isEnd:bool=False):
        self.links = None # Letters that exist at this level of tree
        self.isEnd = isEnd # Indicates end of word


class Trie:

    def __init__(self):
        self.root = TrieNode()

    '''Inserts the string word into the trie.'''
    def insert(self, word: str) -> None:
        node = self.root # Current node
        
        for char in word:

            # Create array of letters to populate if non-existent
            if not node.links:
                node.links = [None]*R

            # Check if array of letters already contains current character
            # If not, add another trie node 
            if not node.links[ord(char) - ord('a')]:
                node.links[ord(char) - ord('a')] = TrieNode()
            
            # Updates current node
            node = node.links[ord(char) - ord('a')]

        # Sets last node / last letter as end
        node.isEnd = True
     

    '''Returns true if the string word is in the trie 
    (i.e., was inserted before), and false otherwise.'''
    def search(self, word: str) -> bool:
        node = self.root # Current node

        # Iterate through each letter of word to search for
        for char in word:

            # Check if letter exists at current TrieNode
            # If yes, continues; 
            # otherwise, stop because the word doesn't exist in this tree
            if node.links and node.links[ord(char) - ord('a')]:
                node = node.links[ord(char) - ord('a')]
            else:
                return False

        # We've only successfully found the word if
        # the last node is the end
        if node.isEnd:
            return True
        return False
        

    '''Returns true if there is a previously inserted string word 
    that has the prefix prefix, and false otherwise.'''
    def startsWith(self, prefix: str) -> bool:
        # Same code as self.search except we don't
        # need to check if the last node is the end
        # since we're only looking for the prefix
        
        node = self.root # Current node

        for char in prefix:
            if node.links and node.links[ord(char) - ord('a')]:
                node = node.links[ord(char) - ord('a')]
            else:
                return False

        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)