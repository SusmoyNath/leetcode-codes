class Solution {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        string word = "";
    };

    class Trie {
    public:
        TrieNode* root;
        Trie() { root = new TrieNode(); }
        
        void insert(string word) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c))
                    node->children[c] = new TrieNode();
                node = node->children[c];
            }
            node->word = word;
        }
    };

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        int m = board.size(), n = board[0].size();
        Trie trie;
        for (string word : words) trie.insert(word);
        
        vector<string> result;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (trie.root->children.count(board[i][j])) {
                    dfs(board, i, j, trie.root, result);
                }
            }
        }
        return result;
    }

private:
    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, vector<string>& result) {
        char c = board[i][j];
        if (!node->children.count(c)) return;

        TrieNode* nextNode = node->children[c];
        if (!nextNode->word.empty()) {
            result.push_back(nextNode->word);
            nextNode->word = "";  // Avoid duplicates
        }

        board[i][j] = '#';  // Mark visited

        vector<int> dirs = {-1, 0, 1, 0, -1}; // Up, Right, Down, Left
        for (int d = 0; d < 4; d++) {
            int ni = i + dirs[d], nj = j + dirs[d + 1];
            if (ni >= 0 && ni < board.size() && nj >= 0 && nj < board[0].size()) {
                dfs(board, ni, nj, nextNode, result);
            }
        }

        board[i][j] = c; // Restore for backtracking

        // Optimization: Remove leaf node from Trie
        if (nextNode->children.empty()) {
            node->children.erase(c);
        }
    }
};
