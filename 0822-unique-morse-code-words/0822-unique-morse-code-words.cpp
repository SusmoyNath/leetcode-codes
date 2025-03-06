class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                                "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                                "..-","...-",".--","-..-","-.--","--.."};
        
        unordered_set<string> transformations;

        for (const string& word : words) {
            string morseWord;
            for (char c : word) {
                morseWord += morse[c - 'a'];  // Convert letter to Morse
            }
            transformations.insert(morseWord);
        }
        
        return transformations.size();
    }
};
