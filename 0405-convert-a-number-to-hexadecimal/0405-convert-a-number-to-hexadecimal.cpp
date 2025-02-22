class Solution {
public:
    string toHex(int num) {
        if (num == 0) return "0";  // Edge case for zero
        
        string hexMap = "0123456789abcdef";
        string result = "";
        
        // Process up to 8 hex digits (32 bits = 8 hex digits)
        for (int i = 0; i < 8 && num != 0; i++) {
            int digit = num & 0xf;  // Extract last 4 bits
            result = hexMap[digit] + result;  // Prepend to result
            num >>= 4;  // Right shift 4 bits
        }
        
        return result;
    }
};
