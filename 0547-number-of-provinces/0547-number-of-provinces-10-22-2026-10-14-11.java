class Solution {
    Map<Integer, Integer> provinces = new HashMap<>(); 

    public int findCircleNum(int[][] isConnected) {
        // first int is the city number
        // second int is the province number (class)   
        int n = isConnected.length;
        int prov = 0;
        for (int city = 0; city < n; city++) {
            if (!this.provinces.containsKey(city)) {
                this.dfs(isConnected, city, prov++);
            }
        }

        return (int) this.provinces.values().stream().distinct().count();
    }

    private void dfs(int[][] isConnected, int city, int prov) {
        if (this.provinces.containsKey(city)) return;
        this.provinces.put(city, prov);
        for (int i = 0; i < isConnected.length; i++) {
            if (isConnected[city][i] == 1) {
                this.dfs(isConnected, i, prov);
            }
        }
    }
}