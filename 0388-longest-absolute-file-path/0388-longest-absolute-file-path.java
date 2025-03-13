class Solution {
    public int lengthLongestPath(String input) {
        String[] entries = input.split("\n");
        int maxLen = 0;
        int[] pathLengths = new int[entries.length + 1]; // Store path lengths at different depths

        for (String entry : entries) {
            int level = entry.lastIndexOf("\t") + 1; // Determine depth based on tabs
            int curLen = pathLengths[level + 1] = pathLengths[level] + entry.length() - level + 1; // +1 for '/'
            
            if (entry.contains(".")) { // If it's a file, update max length
                maxLen = Math.max(maxLen, curLen - 1); // Remove the last '/'
            }
        }

        return maxLen;
    }
}
