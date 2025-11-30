#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n; vector<int> t;
    SegmentTree(const vector<int>& a){
        int sz=a.size(); n=1; while(n<sz) n<<=1;
        t.assign(2*n,0);
        for(int i=0;i<sz;i++) t[n+i]=a[i];
        for(int i=n-1;i>=1;--i) t[i]=t[2*i]+t[2*i+1];
    }
    void update(int idx,int val){
        int i=n+idx; t[i]=val; i>>=1;
        while(i>=1){ t[i]=t[2*i]+t[2*i+1]; i>>=1; }
    }
    int query(int l,int r){
        l+=n; r+=n; int res=0;
        while(l<=r){
            if(l&1) res+=t[l++];
            if(!(r&1)) res+=t[r--];
            l>>=1; r>>=1;
        }
        return res;
    }
};

int main(){
    vector<int> a={1,3,5,7,9,11};
    SegmentTree st(a);
    st.update(1,10);
    int sum = st.query(1,3);
    return 0;
}
