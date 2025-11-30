#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> merge(vector<vector<int>>& in){
    sort(in.begin(), in.end(), [](auto&a,auto&b){return a[0]<b[0];});
    vector<vector<int>> res;
    for(auto &c: in){
        if(res.empty() || res.back()[1] < c[0]) res.push_back(c);
        else res.back()[1] = max(res.back()[1], c[1]);
    } return res;
}
int main(){ return 0; }
