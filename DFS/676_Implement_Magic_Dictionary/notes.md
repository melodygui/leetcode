### Time and Space Complexity

Time Complexity: 
- `buildDict`: for a dictionary with n words, we have to insert each word into the trie, which takes O(l), assuming the average length of the words is l. So overall time complexity is O(n x l).

- `search`: given a word to search, the DFS traversal has to check all l characters of the word. In the worst case (a dense trie where almost every node has all 26 children), if we have not used the one allowed difference, then we will need to check all 25 (assuming 26 is the size of the alphabet of the Trie) characters that do not match the current character. We also need to check the remaining character that does match. 
    - This means worst case time complexity is O(l x 26).

Space Complexity: 
- The main data structure used is trie, which stores a branch for every word for all n words in the dictionary. Worst case, there is no ovelap between the words (all words are completely different). So it takes O(n x l) nodes. 

- The recursion can go up to l levels in depth, adding an additional O(l) space. 

- The dominant factor is the trie storage, so overall space complexity is O(n x l). 