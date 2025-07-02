import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        dfs(0, target, candidates, ans, ds);
        return ans;
    }

    public void dfs(int ind, int target, int[] candidates, List<List<Integer>> ans, List<Integer> ds) {
        if (ind == candidates.length) {
            if (target == 0) {
                ans.add(new ArrayList<>(ds)); // Add a copy of ds
            }
            return;
        }

        // Pick the current element if it's not greater than target
        if (candidates[ind] <= target) {
            ds.add(candidates[ind]);
            dfs(ind, target - candidates[ind], candidates, ans, ds);
            ds.remove(ds.size() - 1); // Backtrack
        }

        // Skip the current element
        dfs(ind + 1, target, candidates, ans, ds);
    }
}
