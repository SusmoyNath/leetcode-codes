class Solution {
    public boolean hasAlternatingBits(int n) {
        int check = n ^ (n >> 1);  // XOR n with its right-shifted version
        return (check & (check + 1)) == 0;  // Ensure all bits are 1
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.hasAlternatingBits(5));  // true (101)
        System.out.println(sol.hasAlternatingBits(7));  // false (111)
        System.out.println(sol.hasAlternatingBits(11)); // false (1011)
    }
}
