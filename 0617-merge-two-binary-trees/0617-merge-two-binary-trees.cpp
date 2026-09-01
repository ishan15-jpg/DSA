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
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if(!root1 || !root2) return root1 ? root1 : root2;
        function<void(TreeNode*,TreeNode*)> help = [&](TreeNode* root1, TreeNode* root2) -> void {
            root1->val = root1->val + root2->val;
            if(root1->left && root2->left) help(root1->left,root2->left);
            if(root1->right && root2->right) help(root1->right,root2->right);
            if(!root1->left){
                root1->left = root2->left;
                root2->left = nullptr;
            }
            if(!root1->right){
                root1->right = root2->right;
                root2->right = nullptr;
            }
        };
        help(root1,root2);
        return root1;
    }
};