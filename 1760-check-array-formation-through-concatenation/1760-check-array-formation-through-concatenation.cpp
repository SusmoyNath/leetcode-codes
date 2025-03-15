class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        unordered_map<int, vector<int>> mp;
        
        // Store the first element of each subarray in the map
        for (const auto& piece : pieces) {
            mp[piece[0]] = piece;
        }
        
        int i = 0, n = arr.size();
        
        while (i < n) {
            // If the current element is not the start of any piece, return false
            if (mp.find(arr[i]) == mp.end()) {
                return false;
            }
            
            // Get the corresponding subarray from pieces
            vector<int>& piece = mp[arr[i]];
            
            // Check if elements in arr match the subarray exactly
            for (int num : piece) {
                if (i < n && arr[i] == num) {
                    i++;
                } else {
                    return false;
                }
            }
        }
        
        return true;
    }
};
