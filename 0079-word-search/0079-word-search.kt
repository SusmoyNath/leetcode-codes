class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val m = board.size
        val n = board[0].size

        // Helper function to perform DFS
        fun dfs(i: Int, j: Int, wordIndex: Int): Boolean {
            // Base case: if we have matched all characters of the word
            if (wordIndex == word.length) {
                return true
            }

            // Check boundaries and whether the current cell matches the current character
            if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[wordIndex]) {
                return false
            }

            // Mark the current cell as visited by temporarily changing its value
            val temp = board[i][j]
            board[i][j] = '#'

            // Explore all four directions (up, down, left, right)
            val directions = arrayOf(
                intArrayOf(1, 0), // down
                intArrayOf(-1, 0), // up
                intArrayOf(0, 1), // right
                intArrayOf(0, -1) // left
            )

            // Recursively search in all directions
            for (dir in directions) {
                val newI = i + dir[0]
                val newJ = j + dir[1]
                if (dfs(newI, newJ, wordIndex + 1)) {
                    return true
                }
            }

            // Backtrack by restoring the original value
            board[i][j] = temp
            return false
        }

        // Start DFS from each cell
        for (i in board.indices) {
            for (j in board[i].indices) {
                if (dfs(i, j, 0)) {
                    return true
                }
            }
        }

        // If no solution is found, return false
        return false
    }
}

fun main() {
    val solution = Solution()
    
    val board1 = arrayOf(
        charArrayOf('A', 'B', 'C', 'E'),
        charArrayOf('S', 'F', 'C', 'S'),
        charArrayOf('A', 'D', 'E', 'E')
    )
    println(solution.exist(board1, "ABCCED")) // Output: true
    
    val board2 = arrayOf(
        charArrayOf('A', 'B', 'C', 'E'),
        charArrayOf('S', 'F', 'C', 'S'),
        charArrayOf('A', 'D', 'E', 'E')
    )
    println(solution.exist(board2, "SEE")) // Output: true
    
    val board3 = arrayOf(
        charArrayOf('A', 'B', 'C', 'E'),
        charArrayOf('S', 'F', 'C', 'S'),
        charArrayOf('A', 'D', 'E', 'E')
    )
    println(solution.exist(board3, "ABCB")) // Output: false
}
