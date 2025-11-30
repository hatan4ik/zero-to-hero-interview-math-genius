#include <bits/stdc++.h>
using namespace std;
vector<int> twoSum(vector<int>& nums, int target){
    unordered_map<int,int> seen;
    for(int i=0;i<(int)nums.size();++i){
        int need = target - nums[i];
        if(seen.count(need)) return {seen[need], i};
        seen[nums[i]] = i;
    }
    return {};
}
int main(){ vector<int> a={2,7,11,15}; auto r=twoSum(a,9); return 0; }
