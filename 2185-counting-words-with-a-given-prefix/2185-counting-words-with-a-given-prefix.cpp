class TrieNode{
    public:
    vector<TrieNode*> children;
    int count;

    TrieNode(){
        this->children.resize(26,nullptr);
        this->count = 0;
    }
};

class Trie{
    public:
    TrieNode* root;

    Trie(){
        root = new TrieNode();
    }

    void add(vector<string>& words){
        for(const string word : words){
            TrieNode* curr = this->root;
            for(const char c : word){
                if(!curr->children[c - 'a']) 
                curr->children[c - 'a'] = new TrieNode();
                curr = curr->children[c - 'a'];
                ++curr->count;
            }
        }
    }

    int getPrefixCount(string& pref){
        TrieNode* curr = this->root;
        for(const char c : pref){
            if(!curr->children[c - 'a']) return 0;
            curr = curr->children[c - 'a'];
        }
        return curr->count;
    }

    ~Trie(){
        delete root;
    }
};

class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int res = 0;
        Trie* root = new Trie();
        root->add(words);
        int count = root->getPrefixCount(pref);
        delete root;
        return count;
    }
};