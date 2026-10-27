class Trie {
    Map<Character, Trie> subtries = new HashMap<>();
    int count = 0;

    public Trie() {}
    
    public void insert(String word) {
        if (word.isEmpty()) {
            this.count++;
        } else {
            subtries.computeIfAbsent(word.charAt(0), k -> new Trie()).insert(word.substring(1));
        }
    }
    
    public boolean search(String word) {
        if (word.isEmpty()) return this.count > 0;
        if (!subtries.containsKey(word.charAt(0))) return false;
        return subtries.get(word.charAt(0)).search(word.substring(1));
    }
    
    public boolean startsWith(String prefix) {
        if (prefix.isEmpty()) return true;
        if (!subtries.containsKey(prefix.charAt(0))) return false;
        return subtries.get(prefix.charAt(0)).startsWith(prefix.substring(1));
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */