// Define Solution class (if it's not defined)
class Solution {
    // Your combine method
    fun combine(n: Int, k: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val currentCombination = mutableListOf<Int>()
        
        fun backtrack(start: Int) {
            if (currentCombination.size == k) {
                result.add(ArrayList(currentCombination))
                return
            }
            for (i in start..n) {
                currentCombination.add(i)
                backtrack(i + 1)
                currentCombination.removeAt(currentCombination.size - 1)
            }
        }
        
        backtrack(1)
        return result
    }
}

fun main() {
    val ret = Solution().combine(4, 2)
    // Your print logic
    println(ret)
}
