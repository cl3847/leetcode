class Solution {
    public int jump(int[] nums) {
        int best = 0;
        int count = -1;
        int i = 0;
        while (i < nums.length) {
            int roundBest = best;
            while (i < nums.length && i <= best) {
                int n = nums[i];
                roundBest = Math.max(roundBest, i + n);
                i++;
            }
            best = roundBest;
            count += 1;
        }

        return count;
    }
}