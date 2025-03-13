class Solution {
public:
    struct TrieNode {
        TrieNode* next[2] = {nullptr, nullptr}; // Only two bits (0 or 1)
    };

    class Trie {
    public:
        TrieNode* root;
        Trie() { root = new TrieNode(); }
        
        void insert(int num) {
            TrieNode* node = root;
            for (int i = 31; i >= 0; i--) { // Insert 32-bit representation
                int bit = (num >> i) & 1;
                if (!node->next[bit]) node->next[bit] = new TrieNode();
                node = node->next[bit];
            }
        }
        
        int getMaxXOR(int num) {
            TrieNode* node = root;
            int maxXor = 0;
            for (int i = 31; i >= 0; i--) { // Check 32-bit representation
                int bit = (num >> i) & 1;
                int oppositeBit = 1 - bit;
                if (node->next[oppositeBit]) { 
                    maxXor |= (1 << i); // Set bit in maxXor
                    node = node->next[oppositeBit]; // Move in opposite direction
                } else {
                    node = node->next[bit]; // Move in the same direction
                }
            }
            return maxXor;
        }
    };

    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        int maxXor = 0;
        
        // Insert all numbers into the Trie
        for (int num : nums) trie.insert(num);
        
        // Compute the max XOR
        for (int num : nums) maxXor = max(maxXor, trie.getMaxXOR(num));

        return maxXor;
    }
};
