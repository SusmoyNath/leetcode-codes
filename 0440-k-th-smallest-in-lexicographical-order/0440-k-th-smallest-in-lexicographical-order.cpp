class Solution {
public:
    int findKthNumber(int n, int k) {
        long curr = 1; // Start with prefix 1
        k--; // Since 1 is already counted

        while (k > 0) {
            long count = countSteps(n, curr, curr + 1);
            if (count <= k) {
                k -= count;
                curr++; // Move to the next prefix
            } else {
                k--; // Move deeper
                curr *= 10;
            }
        }
        return curr;
    }

private:
    long countSteps(long n, long first, long last) {
        long count = 0;
        while (first <= n) {
            count += min(n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return count;
    }
};
