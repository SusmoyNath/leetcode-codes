class WordDictionary {
private:
    struct TrieNode {
        TrieNode* children[26] = {};  // 26 letters
        bool isEnd = false;  // Marks end of a word
    };
    
    TrieNode* root;
    
    bool dfs(TrieNode* node, const string& word, int index) {
        if (!node) return false;  // If the node is null, return false
        if (index == word.size()) return node->isEnd;  // If at end, check isEnd
        
        char ch = word[index];
        
        if (ch == '.') {
            for (int i = 0; i < 26; ++i) {  // Try all possible characters
                if (dfs(node->children[i], word, index + 1)) return true;
            }
            return false;
        } else {
            return dfs(node->children[ch - 'a'], word, index + 1);
        }
    }

public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (!node->children[ch - 'a']) node->children[ch - 'a'] = new TrieNode();
            node = node->children[ch - 'a'];
        }
        node->isEnd = true;
    }
    
    bool search(string word) {
        return dfs(root, word, 0);
    }
};