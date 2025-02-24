class Solution {
public:
    bool isNumber(string s) {
        int i = 0, n = s.size();
        bool hasNum = false, hasDot = false, hasExp = false;

        // Remove leading and trailing spaces
        while (i < n && s[i] == ' ') i++; // Trim left spaces
        if (i < n && (s[i] == '+' || s[i] == '-')) i++; // Optional sign
        
        while (i < n && isdigit(s[i])) { hasNum = true; i++; } // Process integer part
        
        if (i < n && s[i] == '.') { // Handle decimal
            i++;
            while (i < n && isdigit(s[i])) { hasNum = true; i++; } // Process fraction part
        }
        
        if (!hasNum) return false; // There must be at least one digit before or after '.'
        
        if (i < n && (s[i] == 'e' || s[i] == 'E')) { // Handle exponent
            i++;
            if (i < n && (s[i] == '+' || s[i] == '-')) i++; // Optional sign
            bool hasExpNum = false;
            while (i < n && isdigit(s[i])) { hasExpNum = true; i++; } // Process exponent digits
            if (!hasExpNum) return false; // `e` must be followed by digits
        }
        
        while (i < n && s[i] == ' ') i++; // Trim right spaces
        
        return i == n; // Ensure all characters were valid
    }
};
