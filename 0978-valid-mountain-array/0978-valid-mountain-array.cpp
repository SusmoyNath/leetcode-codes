class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        if (n < 3) return false; // A valid mountain needs at least 3 elements

        int i = 0;
        
        // Step 1: Walk up (increasing sequence)
        while (i + 1 < n && arr[i] < arr[i + 1]) {
            i++;
        }
        
        // Peak cannot be the first or last element
        if (i == 0 || i == n - 1) return false;

        // Step 2: Walk down (decreasing sequence)
        while (i + 1 < n && arr[i] > arr[i + 1]) {
            i++;
        }
        
        // If we reached the last index, it is a valid mountain
        return i == n - 1;
    }
};
