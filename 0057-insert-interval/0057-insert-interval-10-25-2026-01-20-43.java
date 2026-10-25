class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> intervalsList = new ArrayList<>(Arrays.asList(intervals));
        int lo = 0, hi = intervals.length;
        int target = newInterval[0];
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (intervals[mid][0] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        System.out.println(lo);
        intervalsList.add(lo, newInterval);

        List<int[]> res = new ArrayList<>();
        int[] prev = intervalsList.get(0);
        for (int i = 1; i < intervalsList.size(); i++) {
            int[] curr = intervalsList.get(i);
            if (curr[0] <= prev[1]) {
                prev[1] = Math.max(prev[1], curr[1]);
            } else {
                res.add(prev);
                prev = curr;
            }
        }
        res.add(prev);

        return res.toArray(new int[0][]);
    }
}