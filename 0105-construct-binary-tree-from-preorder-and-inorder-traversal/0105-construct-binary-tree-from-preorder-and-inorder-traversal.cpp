/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size() == 1){
            TreeNode* node = new TreeNode(preorder[0]);
            return node;
        }

        int i = 0;

        function<TreeNode*(int,int)> help = [&](int start, int end) -> TreeNode* {
            if(start > end) return nullptr;

            TreeNode* root = new TreeNode(preorder[i]);

            int j = start;
            while(j < end+1){ 
                if(preorder[i] == inorder[j]) break;
                j++;    
            }
            i++;

            root->left = help(start, j-1);
            root->right = help(j+1, end);

            return root;
        };

        return help(0, preorder.size()-1);
    }
};