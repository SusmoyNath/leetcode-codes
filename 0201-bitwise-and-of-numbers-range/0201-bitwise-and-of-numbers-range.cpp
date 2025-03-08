class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        
        // Shift left and right until they become the same
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        
        // Shift back to restore the common prefix
        return left << shift;
    }
};
