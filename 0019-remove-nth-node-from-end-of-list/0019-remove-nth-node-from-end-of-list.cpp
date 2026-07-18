/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n){
        int k = 1;
        function<ListNode*(ListNode*,int&)> help = [&](ListNode* root, int& k) -> ListNode* {
            if(!root) return nullptr;

            ListNode* temp = help(root->next, k);

            if(k == -1){
                root->next = temp;
                return root;
            }

            if(k == n){
                root->next = nullptr;
                delete root;
                k = -1;
                return temp;
            }

            ++k;
            return root;
        };
        return help(head, k);
    }
};