public class Solution {
    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        IList<IList<int>> result = new List<IList<int>>();
        List<int> currentSubset = new List<int>();
        
        // Sort the array to help handle duplicates
        Array.Sort(nums);
        
        // Backtracking function to generate all subsets
        Backtrack(nums, 0, currentSubset, result);
        
        return result;
    }
    
    private void Backtrack(int[] nums, int start, List<int> currentSubset, IList<IList<int>> result) {
        // Add the current subset to the result
        result.Add(new List<int>(currentSubset));
        
        // Iterate over the elements starting from 'start'
        for (int i = start; i < nums.Length; i++) {
            // Skip duplicates by ensuring we don't pick the same element twice
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // Add the current element to the subset
            currentSubset.Add(nums[i]);
            
            // Recurse to generate all subsets that include nums[i]
            Backtrack(nums, i + 1, currentSubset, result);
            
            // Backtrack: remove the last element added
            currentSubset.RemoveAt(currentSubset.Count - 1);
        }
    }
}
