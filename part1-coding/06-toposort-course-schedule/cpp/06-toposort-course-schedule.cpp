#include <bits/stdc++.h>
using namespace std;
vector<int> topoSort(int n, vector<pair<int,int>>& edges){
    vector<vector<int>> g(n); vector<int> indeg(n);
    for(auto &e: edges){ g[e.second].push_back(e.first); indeg[e.first]++; }
    queue<int> q; for(int i=0;i<n;i++) if(indeg[i]==0) q.push(i);
    vector<int> ord;
    while(!q.empty()){
        int u=q.front(); q.pop(); ord.push_back(u);
        for(int v: g[u]) if(--indeg[v]==0) q.push(v);
    }
    return (int)ord.size()==n?ord:vector<int>{};
}
int main(){ return 0; }
