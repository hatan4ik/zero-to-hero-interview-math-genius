public class SegmentTreeRangeQuery {
    int n; int[] t;
    public SegmentTreeRangeQuery(int[] a){
        n=1; while(n<a.length) n<<=1;
        t=new int[2*n];
        for(int i=0;i<a.length;i++) t[n+i]=a[i];
        for(int i=n-1;i>=1;--i) t[i]=t[2*i]+t[2*i+1];
    }
    public void update(int idx,int val){
        int i=n+idx; t[i]=val; i>>=1;
        while(i>=1){ t[i]=t[2*i]+t[2*i+1]; i>>=1; }
    }
    public int query(int l,int r){
        l+=n; r+=n; int res=0;
        while(l<=r){
            if((l&1)==1) res+=t[l++];
            if((r&1)==0) res+=t[r--];
            l>>=1; r>>=1;
        }
        return res;
    }
    public static void main(String[] args){
        int[] a={1,3,5,7,9,11};
        SegmentTreeRangeQuery st=new SegmentTreeRangeQuery(a);
        st.update(1,10);
        int sum=st.query(1,3);
    }
}
