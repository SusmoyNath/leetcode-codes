class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> bankSet(bank.begin(), bank.end()); // Convert bank to a set
        if (bankSet.find(endGene) == bankSet.end()) return -1; // If endGene is not in bank, return -1

        queue<pair<string, int>> q; // (gene, mutationCount)
        q.push({startGene, 0});
        
        vector<char> mutations = {'A', 'C', 'G', 'T'};

        while (!q.empty()) {
            auto [current, mutationsCount] = q.front();
            q.pop();

            // If we reached the endGene, return the number of mutations
            if (current == endGene) return mutationsCount;

            // Try mutating each character
            for (int i = 0; i < 8; i++) {
                char originalChar = current[i];

                for (char c : mutations) {
                    if (c == originalChar) continue; // Skip same character mutation
                    
                    current[i] = c; // Mutate
                    if (bankSet.find(current) != bankSet.end()) {
                        q.push({current, mutationsCount + 1});
                        bankSet.erase(current); // Remove from bank to prevent revisiting
                    }
                }

                current[i] = originalChar; // Revert mutation
            }
        }

        return -1; // No valid mutation sequence found
    }
};
