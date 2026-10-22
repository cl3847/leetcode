class Solution {
    public boolean canJump(int[] nums) {
        int best = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > best) return false;
            best = Math.max(best, i + nums[i]);
        }
        return best >= nums.length - 1;
    }
}