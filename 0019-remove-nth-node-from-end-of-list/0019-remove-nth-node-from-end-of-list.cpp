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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* left = head;
        ListNode* right = head;
        while(n--) right = right->next;
        ListNode* temp = nullptr;
        while(right){
            temp = left;
            left = left->next;
            right = right->next;
        }
        if(!temp){
            temp = left->next;
            delete left;
            return temp;
        }
        temp->next = left->next;
        left->next = nullptr;
        delete left;
        return head;
    }
};