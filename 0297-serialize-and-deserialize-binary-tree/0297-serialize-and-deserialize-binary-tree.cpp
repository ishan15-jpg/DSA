/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
    vector<string> splitStr(string data){
        vector<string> arr;
        int i = 0;
        string temp = "";
        while(i < data.length()){
            if(data[i] == ','){
                arr.push_back(temp);
                temp = "";
                ++i;
                continue;
            }
            temp += data[i];
            ++i;
        }
        return arr;
    }

public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(!root) return "";
        string serTree = "";
        function<string(TreeNode* root)> dfs = [&](TreeNode* root) -> string {
            if(!root) return "N,";
            string curr = to_string(root->val) + ",";
            curr += dfs(root->left);
            curr += dfs(root->right);
            return curr;
        };
        string serializedTree = dfs(root);
        return serializedTree.substr(0,serializedTree.length()-1);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.empty()) return nullptr;
        vector<string> dataArr = this->splitStr(data);
        int i = 0;
        function<TreeNode*()> dfs = [&]() -> TreeNode* {
            if(i >= dataArr.size()) return nullptr;
            if(dataArr[i] == "N") return nullptr;
            TreeNode* node = new TreeNode(stoi(dataArr[i]));
            i += 1;
            node->left = dfs();
            i += 1;
            node->right = dfs();
            return node;
        };
        return dfs();
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));