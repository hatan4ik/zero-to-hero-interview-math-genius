#include <bits/stdc++.h>
using namespace std;
vector<int> twoSum(vector<int>& nums, int target); // decl

int main(){
    vector<int> a={2,7,11,15};
    auto r=twoSum(a,9);
    assert(r.size()==2 && r[0]==0 && r[1]==1);
    cout << "C++ two_sum OK\n";
    return 0;
}
