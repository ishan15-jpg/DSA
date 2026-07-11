class TrieNode {
    public:
    vector<TrieNode*> child{26, NULL};
    bool isTerminal = false;
};

class Trie {
    TrieNode* root = NULL;
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        function<void(TrieNode*,string)> util = [&](TrieNode* root, string word) {
            if(word.length() == 0){
                root->isTerminal = true;
                return;
            }
            int idx = word[0] - 'a';
            if(root->child[idx]) util(root->child[idx], word.substr(1));
            else{ 
                TrieNode* newNode = new TrieNode();
                root->child[idx] = newNode;
                util(newNode,word.substr(1));
            }
        };
        util(this->root,word);
    }
    
    bool search(string word) {
        function<bool(TrieNode*,string)> util = [&](TrieNode* root, string word) -> bool {
            if(word.length() == 0) return root->isTerminal;

            int idx = word[0] - 'a';

            if(!root->child[idx]) return false;

            return util(root->child[idx], word.substr(1));
        };
        return util(this->root, word);
    }
    
    bool startsWith(string prefix) {
        function<bool(TrieNode*,string)> util = [&](TrieNode* root, string prefix) -> bool {
            if(prefix.length() == 0) return true;

            int idx = prefix[0] - 'a';

            if(!root->child[idx]) return false;

            return util(root->child[idx], prefix.substr(1));
        };
        return util(this->root, prefix);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */