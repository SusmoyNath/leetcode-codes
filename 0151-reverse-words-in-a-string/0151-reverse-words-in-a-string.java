class Solution {
    public String reverseWords(String s) {
        // Trim leading/trailing spaces and split by whitespace
        String[] words = s.trim().split("\\s+");  
        
        // Reverse the words using StringBuilder
        StringBuilder result = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            result.append(words[i]).append(" ");
        }
        
        // Remove the extra trailing space at the end
        return result.toString().trim();
    }
}
