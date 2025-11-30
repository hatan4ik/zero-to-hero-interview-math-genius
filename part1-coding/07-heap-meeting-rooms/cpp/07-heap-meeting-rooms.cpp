#include <bits/stdc++.h>
using namespace std;
int minMeetingRooms(vector<vector<int>>& in){
    sort(in.begin(), in.end(), [](auto&a,auto&b){return a[0]<b[0];});
    priority_queue<int, vector<int>, greater<int>> pq;
    for(auto &m: in){
        if(!pq.empty() && pq.top() <= m[0]) pq.pop();
        pq.push(m[1]);
    }
    return (int)pq.size();
}
int main(){ return 0; }
