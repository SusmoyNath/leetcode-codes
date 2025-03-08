class Trie {
private:
    struct TrieNode {
        TrieNode* children[26]; // Array for 26 lowercase letters
        bool isEndOfWord; // Marks the end of a valid word
        
        TrieNode() {
            isEndOfWord = false;
            for (int i = 0; i < 26; i++) children[i] = nullptr;
        }
    };

    TrieNode* root; // Root of the Trie

public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            int index = ch - 'a'; // Map character to index (0-25)
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->isEndOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            int index = ch - 'a';
            if (node->children[index] == nullptr) return false;
            node = node->children[index];
        }
        return node->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            int index = ch - 'a';
            if (node->children[index] == nullptr) return false;
            node = node->children[index];
        }
        return true;
    }
};
