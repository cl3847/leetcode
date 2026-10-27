class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        Map<String, List<Integer>> workerEntries = new HashMap<>();
        for (int i = 0; i < keyName.length; i++) {
            String worker = keyName[i];
            String[] timeParts = keyTime[i].split(":");
            int minutes = Integer.parseInt(timeParts[0]) * 60 + Integer.parseInt(timeParts[1]);

            workerEntries.computeIfAbsent(worker, k -> new ArrayList<>()).add(minutes);
        }

        List<String> alerted = new ArrayList<>();
        for (String worker : workerEntries.keySet()) {
            List<Integer> times = workerEntries.get(worker);
            times.sort(Comparator.naturalOrder());
            for (int j = 1; j < times.size() - 1; j++) {
                if (times.get(j+1) - times.get(j-1) <= 60) {
                    alerted.add(worker);
                    break;
                }
            }
        }

        alerted.sort(Comparator.naturalOrder());
        return alerted;
    }
}