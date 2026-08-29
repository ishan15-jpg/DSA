class TrieNode{
    public TrieNode[] children;
    public int count;

    public TrieNode(){
        this.children = new TrieNode[26];
        this.count = 0;
    }
}

class Trie{
    TrieNode root;

    public Trie(){
        this.root = new TrieNode();
    }

    public void add(String[] words){
        for(String word : words){
            TrieNode curr = this.root;
            for(char c : word.toCharArray()){
                int idx = c - 'a';
                if(curr.children[idx] == null)
                curr.children[idx] = new TrieNode();
                curr = curr.children[idx];
                ++curr.count;
            }
        }
    }

    public int getPrefixCount(String pref){
        TrieNode curr = this.root;
        for(char c : pref.toCharArray()){
            if(curr.children[c - 'a'] == null) return 0;
            curr = curr.children[c - 'a'];
        }
        return curr.count;
    }
}

class Solution {
    public int prefixCount(String[] words, String pref) {
        Trie root = new Trie();
        root.add(words);
        return root.getPrefixCount(pref);
    }
}