class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> nums; // Stores available numbers
        int fact = 1; // Factorial of (n-1), (n-2), ...
        string result = "";

        // Precompute numbers and factorial
        for (int i = 1; i <= n; i++) {
            nums.push_back(i);
            fact *= i;
        }

        // Convert k to zero-based index
        k--;

        // Build the k-th permutation
        for (int i = n; i > 0; i--) {
            fact /= i; // Update factorial for next step
            int index = k / fact; // Select digit
            result += to_string(nums[index]); // Append to result
            nums.erase(nums.begin() + index); // Remove used digit
            k %= fact; // Update k for next step
        }

        return result;
    }
};
