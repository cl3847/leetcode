class Solution {
    public int findCircleNum(int[][] isConnected) {
        Set<Integer> seen = new HashSet<>();
        int n = isConnected.length;
        int prov = 0;
        for (int city = 0; city < n; city++) {
            if (!seen.contains(city)) {
                this.dfs(isConnected, seen, city, prov++);
            }
        }

        return prov;
    }

    private void dfs(int[][] isConnected, Set seen, int city, int prov) {
        seen.add(city);
        for (int i = 0; i < isConnected.length; i++) {
            if (isConnected[city][i] == 1 && !seen.contains(i)) {
                this.dfs(isConnected, seen, i, prov);
            }
        }
    }
}