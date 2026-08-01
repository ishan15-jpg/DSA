class TrieNode {
    public TrieNode[] child;
    public boolean isTerminal;

    public TrieNode(){
        this.child = new TrieNode[26];
        this.isTerminal = false;
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        this.root = new TrieNode();        
    }
    
    private void insertUtil(String word, TrieNode root){
        if(word.length() == 0){
            root.isTerminal = true;
            return;
        }
        int key = word.charAt(0) - 'a';
        if(root.child[key] == null) root.child[key] = new TrieNode();
        this.insertUtil(word.substring(1), root.child[key]);
    }

    public void insert(String word) {
        this.insertUtil(word, this.root);
    }

    private boolean searchUtil(String word, TrieNode root){
        if(word.length() == 0) return root.isTerminal;
        int key = word.charAt(0) - 'a';
        if(root.child[key] == null) return false;
        return this.searchUtil(word.substring(1), root.child[key]);
    }
    
    public boolean search(String word) {
        return this.searchUtil(word, this.root);
    }
    
    private boolean startsWithUtil(String prefix, TrieNode root){
        if(prefix.length() == 0) return true;
        int key = prefix.charAt(0) - 'a';
        if(root.child[key] == null) return false;
        return this.startsWithUtil(prefix.substring(1), root.child[key]);
    }

    public boolean startsWith(String prefix) {
        return this.startsWithUtil(prefix, this.root);
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */