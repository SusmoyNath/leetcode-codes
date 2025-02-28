class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val currentSubset = mutableListOf<Int>()

        fun backtrack(index: Int) {
            // Add the current subset to the result
            result.add(ArrayList(currentSubset))

            // Explore further by including each element starting from 'index'
            for (i in index until nums.size) {
                currentSubset.add(nums[i])  // Include the element
                backtrack(i + 1)  // Recurse with the next index
                currentSubset.removeAt(currentSubset.size - 1)  // Exclude the element
            }
        }

        backtrack(0)  // Start recursion from the first index
        return result
    }
}

fun main() {
    val solution = Solution()
    val nums = intArrayOf(1, 2, 3)
    val result = solution.subsets(nums)
    
    // Print the result
    println(result)
}
