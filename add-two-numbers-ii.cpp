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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* temp = l1;
        vector<int> stackl1;
        while(temp != nullptr){
            stackl1.push_back(temp->val);
            temp = temp->next;
        }

        temp = l2;
        vector<int> stackl2;
        while(temp != nullptr){
            stackl2.push_back(temp->val);
            temp = temp->next;
        }

        ListNode* ans;
        int carry = 0;
        while(stackl1.size() > 0 && stackl2.size() > 0){
            temp = ans;
            int sum = stackl1[stackl1.size()-1] + stackl2[stackl2.size()-1] + carry;
            stackl1.pop_back();
            stackl2.pop_back();

            carry = sum/10;

            ans = new ListNode();
            ans->next = temp;
            ans->val = sum%10;

        }

        for (auto it =  stackl1.rbegin(); it != stackl1.rend(); ++it){
            temp = ans;

            int sum = *it + carry;

            carry = sum/10;

            ans = new ListNode();
            ans->next = temp;
            ans->val = sum%10;
        }
        for (auto it =  stackl2.rbegin(); it != stackl2.rend(); ++it){
            temp = ans;

            int sum = *it + carry;

            carry = sum/10;

            ans = new ListNode();
            ans->next = temp;
            ans->val = sum%10;
        }

        if(carry != 0){
            temp = ans;
            ans = new ListNode();
            ans->next = temp;
            ans->val = carry;
        }

        return ans;
    }
};