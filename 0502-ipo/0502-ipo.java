import java.util.PriorityQueue;
import java.util.Arrays;

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;

        // Min-Heap to store (capital, profit) pairs sorted by capital
        PriorityQueue<int[]> minCapitalHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        // Max-Heap to store profits of affordable projects
        PriorityQueue<Integer> maxProfitHeap = new PriorityQueue<>((a, b) -> b - a);

        // Insert all projects into minCapitalHeap
        for (int i = 0; i < n; i++) {
            minCapitalHeap.offer(new int[]{capital[i], profits[i]});
        }

        // Select up to k projects
        for (int i = 0; i < k; i++) {
            // Move all affordable projects into maxProfitHeap
            while (!minCapitalHeap.isEmpty() && minCapitalHeap.peek()[0] <= w) {
                maxProfitHeap.offer(minCapitalHeap.poll()[1]); // Push the profit
            }

            // If no project is affordable, break
            if (maxProfitHeap.isEmpty()) break;

            // Select the most profitable project
            w += maxProfitHeap.poll();
        }

        return w;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int k = 2, w = 0;
        int[] profits = {1, 2, 3};
        int[] capital = {0, 1, 1};

        System.out.println(sol.findMaximizedCapital(k, w, profits, capital)); // Output: 4
    }
}
