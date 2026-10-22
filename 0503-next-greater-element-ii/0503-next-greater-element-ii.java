class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        Arrays.fill(res, -1);

        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < 2 * nums.length; i++) {
            int j = i % nums.length;
            int n = nums[j];
            while (stack.size() > 0 && nums[stack.peek()] < n) {
                int removed = stack.pop();
                res[removed] = n;
            }
            if (i == j) stack.push(j);
        }

        return res;
    }
}