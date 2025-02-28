class Solution:
    def numTrees(self, n: int) -> int:
        # Create a DP array to store the number of unique BSTs for each node count
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1  # There's one BST for an empty tree
        dp[1] = 1  # There's one BST for a tree with one node

        # Fill the DP array for values from 2 to n
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]

# Example usage:
solution = Solution()
n = 3  # You can change this value to test with different inputs
print(f"Number of unique BSTs for n = {n}: {solution.numTrees(n)}")
