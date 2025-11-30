#include <bits/stdc++.h>
using namespace std;
int minMeetingRooms(vector<vector<int>>& in);
int main(){
    vector<vector<int>> v={{0,30},{5,10},{15,20}};
    assert(minMeetingRooms(v)==2);
    cout<<"C++ heap OK\n";
    return 0;
}
