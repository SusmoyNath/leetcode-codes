class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i = 0, j = 0;

        while (j < typed.length()) {
            if (i < name.length() && name.charAt(i) == typed.charAt(j)) {
                i++;  // Move both pointers forward when characters match
            } else if (j == 0 || typed.charAt(j) != typed.charAt(j - 1)) {
                return false;  // If the current char is not a long-press of the previous char
            }
            j++;  // Always move forward in 'typed'
        }

        return i == name.length();  // Ensure all characters in 'name' were used
    }
}
