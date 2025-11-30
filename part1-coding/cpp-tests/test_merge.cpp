#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> merge(vector<vector<int>>& in);
int main(){
    vector<vector<int>> in={{1,3},{2,6},{8,10},{15,18}};
    auto out=merge(in);
    assert(out.size()==3 && out[0][0]==1 && out[0][1]==6);
    cout<<"C++ merge OK\n";
    return 0;
}
