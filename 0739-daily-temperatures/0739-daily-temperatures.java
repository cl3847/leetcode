class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];

        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < temperatures.length; i++) {
            int n = temperatures[i];
            while (stack.size() > 0 && temperatures[stack.peek()] < n) {
                int removed = stack.pop();
                res[removed] = i - removed;
            }
            stack.push(i);
        }
        
        return res;
    }
}