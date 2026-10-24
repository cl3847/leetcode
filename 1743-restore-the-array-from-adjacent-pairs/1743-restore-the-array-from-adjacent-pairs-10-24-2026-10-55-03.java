class Solution {
    public int[] restoreArray(int[][] adjacentPairs) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        Set<Integer> singles = new HashSet<>();
        for (int i = 0; i < adjacentPairs.length; i++) {
            int u = adjacentPairs[i][0], v = adjacentPairs[i][1];
            adjList.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            adjList.computeIfAbsent(v, k -> new ArrayList<>()).add(u);

            if (!singles.remove(u)) singles.add(u);
            if (!singles.remove(v)) singles.add(v);
        }

        int n = adjList.size();
        int[] res = new int[n];
        res[0] = singles.iterator().next();
        res[1] = adjList.get(res[0]).get(0); // should only have one item
        for (int i = 2; i < n; i++) {
            List<Integer> candidates = adjList.get(res[i-1]);
            res[i] = (res[i-2] == candidates.get(0)) ? candidates.get(1) : candidates.get(0);
        }

        return res;
    }
}