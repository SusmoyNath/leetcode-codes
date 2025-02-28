public class Solution {
    public IList<int> GrayCode(int n) {
        IList<int> result = new List<int>();
        result.Add(0);  // Start with 0
        
        for (int i = 0; i < n; i++) {
            int size = result.Count;
            // Create new values by adding a 1 at the i-th bit position
            for (int j = size - 1; j >= 0; j--) {
                result.Add(result[j] | (1 << i));
            }
        }
        
        return result;
    }
}
