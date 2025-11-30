#include <bits/stdc++.h>
using namespace std;
struct Node{ int val; Node*left; Node*right; Node(int v):val(v),left(NULL),right(NULL){} };
vector<vector<int>> levelOrder(Node* root){
    vector<vector<int>> res; if(!root) return res;
    queue<Node*> q; q.push(root);
    while(!q.empty()){
        int sz=q.size(); vector<int> lvl;
        for(int i=0;i<sz;++i){
            Node* n=q.front(); q.pop(); lvl.push_back(n->val);
            if(n->left) q.push(n->left);
            if(n->right) q.push(n->right);
        } res.push_back(lvl);
    } return res;
}
int main(){ return 0; }
