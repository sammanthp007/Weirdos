#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <climits>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

class LinkedListNode {
public:
    int val;
    LinkedListNode* next;

    LinkedListNode(int value) {
        val = value;
        next = NULL;
    }
};

LinkedListNode* insert_node_into_singly_linked_list(LinkedListNode* head, int val) {
    if(head == NULL) {
        head = new LinkedListNode(val);
    }
    else {
        LinkedListNode* iter = head;
        while(iter->next != NULL) {
            iter = iter->next;
        }
        LinkedListNode* node = new LinkedListNode(val);
        iter->next = node;
    }
    
    return head;
}


/*
 * For reference:
 * LinkedListNode {
 *     int val;
 *     LinkedListNode* next;
 * };
 *
 * Write your code below.
*/
LinkedListNode* optimal(LinkedListNode* head) {
    if (head == NULL) {
        return NULL;
    }
    LinkedListNode* current_ptr = head;
    LinkedListNode* return_curr_ptr = head;
    set<int> s;
    s.insert(current_ptr->val);
    while (current_ptr != NULL)
        {
        if (s.find(current_ptr->val) != s.end()){
            current_ptr = current_ptr->next;
        }
        else {
            s.insert(current_ptr->val);
            return_curr_ptr->next = current_ptr;
            return_curr_ptr = return_curr_ptr->next;
            current_ptr = current_ptr->next;
        }
    }
    return_curr_ptr->next = NULL;
    return head;
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    
    int n;
    int value;
    LinkedListNode* head = NULL;
    cin >> n;
    for(int i = 0; i < n; i++) { 
        cin >> value;
        head = insert_node_into_singly_linked_list(head, value);
    }
    
    LinkedListNode* res = optimal(head);
    while(res != NULL) {
        fout << res->val << endl;
        
        res = res->next;
    }
    
    fout.close();
    return 0;
}