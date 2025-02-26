import java.util.*;

class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> result = new ArrayList<>();
        Map<String, Integer> wordMap = new HashMap<>();
        
        // Store all words and their indices in a hashmap
        for (int i = 0; i < words.length; i++) {
            wordMap.put(words[i], i);
        }

        // Iterate through each word
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            int n = word.length();

            for (int j = 0; j <= n; j++) {
                // Split word into prefix & suffix
                String prefix = word.substring(0, j);
                String suffix = word.substring(j);

                // Case 1: If prefix is a palindrome & reversed suffix exists
                if (isPalindrome(prefix)) {
                    String reversedSuffix = new StringBuilder(suffix).reverse().toString();
                    if (wordMap.containsKey(reversedSuffix) && wordMap.get(reversedSuffix) != i) {
                        result.add(Arrays.asList(wordMap.get(reversedSuffix), i));
                    }
                }

                // Case 2: If suffix is a palindrome & reversed prefix exists
                // We skip j == n to avoid duplicates (checking full word again)
                if (j != n && isPalindrome(suffix)) {
                    String reversedPrefix = new StringBuilder(prefix).reverse().toString();
                    if (wordMap.containsKey(reversedPrefix) && wordMap.get(reversedPrefix) != i) {
                        result.add(Arrays.asList(i, wordMap.get(reversedPrefix)));
                    }
                }
            }
        }

        return result;
    }

    // Helper function to check if a string is a palindrome
    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) return false;
        }
        return true;
    }
}
