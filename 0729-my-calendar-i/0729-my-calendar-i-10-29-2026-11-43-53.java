class MyCalendar {
    TreeMap<Integer, Integer> bookings = new TreeMap<>();

    public MyCalendar() {
        bookings.put(Integer.MAX_VALUE, Integer.MAX_VALUE);
    }
    
    public boolean book(int startTime, int endTime) {
        Map.Entry<Integer, Integer> pair = bookings.higherEntry(startTime);
        boolean res = endTime <= pair.getValue();
        if (res) bookings.put(endTime, startTime);
        return res;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(startTime,endTime);
 */