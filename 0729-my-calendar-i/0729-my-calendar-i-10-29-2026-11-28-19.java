class MyCalendar {
    List<Pair<Integer, Integer>> bookedTimes = new ArrayList<>();

    public MyCalendar() {
        
    }
    
    public boolean book(int startTime, int endTime) {
        int lo = 0, hi = bookedTimes.size();
        if (hi > 0) {
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (startTime < bookedTimes.get(mid).getKey()) {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            if (lo > 0 && bookedTimes.get(lo-1).getValue() > startTime) return false;
            if (lo < bookedTimes.size() && bookedTimes.get(lo).getKey() < endTime) return false;
        }
        bookedTimes.add(lo, new Pair(startTime, endTime));
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(startTime,endTime);
 */