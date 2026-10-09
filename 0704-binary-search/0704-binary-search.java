class Solution {
    public int search(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length;

        while (lo < hi) {
            int res = lo + (hi-lo)/2;
            if (nums[res] < target) {
                lo = res + 1;
            } else if (nums[res] > target) {
                hi = res;
            } else {
                return res;
            }  
        }

        return -1;
    }
}