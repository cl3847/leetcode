class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // naive approach: 3 loops, n^3
        // better approach: sort, then two pointer
        // n log n sort
        // n^2 two pointer

        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        System.out.println(Arrays.toString(nums));
        Integer prevTarget = null;
        for (int i = 0; i < nums.length; i++) {
            int target = -nums[i];
            if (prevTarget != null && target == prevTarget) continue;
            prevTarget = target;

            int front = i + 1, back = nums.length - 1;
            while (front < back) {
                if (nums[front] + nums[back] == target) {
                    List<Integer> triplet = Arrays.asList(nums[i], nums[front], nums[back]);
                    res.add(triplet);
                    
                    int prevFront = nums[front];
                    while (front < back && nums[front] == prevFront) {
                        front++;
                    }

                    int prevBack = nums[back];
                    while (front < back && nums[back] == prevBack) {
                        back--;
                    }
                } else if (nums[front] + nums[back] < target) {
                    front++;
                } else {
                    back--;
                }
            }
        }
        return res;
    }
}