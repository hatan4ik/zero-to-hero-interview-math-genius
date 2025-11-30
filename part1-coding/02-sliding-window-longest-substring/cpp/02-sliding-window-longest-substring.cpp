#include <bits/stdc++.h>
using namespace std;
int lengthOfLongestSubstring(string s){
    unordered_set<char> st; int l=0,b=0;
    for(int r=0;r<(int)s.size();++r){
        while(st.count(s[r])) st.erase(s[l++]);
        st.insert(s[r]); b=max(b, r-l+1);
    }
    return b;
}
int main(){ cout<<lengthOfLongestSubstring("abba")<<"\n"; }
