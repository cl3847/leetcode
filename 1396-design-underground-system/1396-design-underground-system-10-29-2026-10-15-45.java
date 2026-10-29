class UndergroundSystem {
    Map<Integer, Pair<String, Integer>> passengers = new HashMap<>();
    Map<String, Pair<Double, Integer>> travelTimes = new HashMap<>();

    public UndergroundSystem() {}
    
    public void checkIn(int id, String stationName, int t) {
        Pair<String, Integer> p = new Pair(stationName, t);
        this.passengers.put(id, p);
    }
    
    public void checkOut(int id, String stationName, int t) {
        Pair<String, Integer> p = this.passengers.remove(id);
        String journey = p.getKey() + "_" + stationName;
        Pair<Double, Integer> existingPair = this.travelTimes.getOrDefault(journey, new Pair(0.0, 0));
        this.travelTimes.put(
            journey,
            new Pair(existingPair.getKey() + (t - p.getValue()), existingPair.getValue() + 1)
        );
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String journey = startStation + "_" + endStation;
        Pair<Double, Integer> times = this.travelTimes.get(journey);
        return times.getKey() / times.getValue();
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */