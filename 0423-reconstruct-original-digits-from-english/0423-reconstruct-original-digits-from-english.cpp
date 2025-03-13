class Solution {
public:
    string originalDigits(string s) {
        vector<int> count(26, 0); // Letter frequency
        for (char c : s) count[c - 'a']++; 

        vector<int> digitCount(10, 0);

        // Identifying unique digits first
        digitCount[0] = count['z' - 'a']; // "zero"
        digitCount[2] = count['w' - 'a']; // "two"
        digitCount[4] = count['u' - 'a']; // "four"
        digitCount[6] = count['x' - 'a']; // "six"
        digitCount[8] = count['g' - 'a']; // "eight"

        // Now deduce other numbers
        digitCount[1] = count['o' - 'a'] - digitCount[0] - digitCount[2] - digitCount[4]; // "one"
        digitCount[3] = count['h' - 'a'] - digitCount[8]; // "three"
        digitCount[5] = count['f' - 'a'] - digitCount[4]; // "five"
        digitCount[7] = count['s' - 'a'] - digitCount[6]; // "seven"
        digitCount[9] = count['i' - 'a'] - digitCount[5] - digitCount[6] - digitCount[8]; // "nine"

        // Construct output string
        string result;
        for (int i = 0; i <= 9; i++) {
            result.append(digitCount[i], '0' + i);
        }
        
        return result;
    }
};
