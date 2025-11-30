# Segment Tree — Range Query, Point Update


### Mathematical Reasoning
**Range Query Decomposition:** Any range [l,r] can be decomposed into O(log n) canonical segments in a balanced binary tree. Each node represents a range and stores aggregate information.

**Tree Structure:** Complete binary tree where leaves represent array elements and internal nodes store aggregate values (sum, min, max, etc.) of their children's ranges.

**Query Efficiency:** Any range query touches at most 2×⌈log₂ n⌉ nodes by decomposing the query range into disjoint segments that align with tree structure.

**Update Propagation:** Point updates affect exactly ⌈log₂ n⌉ nodes along the path from leaf to root, maintaining tree invariants.

**Lazy Propagation:** Defers range updates using lazy flags, achieving O(log n) range updates by pushing updates down only when necessary.

**Complexity:** Time O(log n) per query/update, O(n) build, Space O(n)

### Visual Representation
```
Array: [1, 3, 5, 7, 9, 11]
Segment Tree for Range Sum Queries:

                    36
                 [0,5]
                /      \
            9              27
         [0,2]          [3,5]
        /     \        /     \
      4         5    16       11
   [0,1]     [2,2] [3,4]   [5,5]
   /   \              /   \
  1     3           7     9
[0,0] [1,1]      [3,3] [4,4]

Query [1,4]: Traverse tree, combine segments [1,1], [2,2], [3,4]
Path: Root → Left → Right(leaf) + Right(leaf) + Right → Left
Result: 3 + 5 + 16 = 24
```

### Range Decomposition Example
```
Query range [2,4] on array of size 6:

Original range: [2,4]
Tree decomposition:
- Node [2,2]: covers index 2 → value 5
- Node [3,4]: covers indices 3,4 → value 16
Total: 5 + 16 = 21

Efficient: Only 2 nodes touched instead of 3 individual elements
```

### Algorithm Invariant
**Tree Invariant:** Each internal node stores the aggregate of all elements in its subtree range, enabling efficient range queries through tree traversal.

### Pseudocode
```
build:
  n = power_of_two >= len(a); tree size = 2n
  fill leaves with a; for i=n-1..1: tree[i]=merge(tree[2i], tree[2i+1])

update(i, val):
  p = n+i; tree[p]=val; p//=2 while p>=1: tree[p]=merge(children); p//=2

query(l,r):  # inclusive
  l+=n; r+=n; res=identity
  while l<=r:
    if l odd: res=merge(res, tree[l]); l++
    if r even: res=merge(res, tree[r]); r--
    l//=2; r//=2
  return res
```

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
class SegmentTree:
    def __init__(self, nums):
        n = len(nums); self.n = 1
        while self.n < n: self.n <<= 1
        self.tree = [0] * (2 * self.n)
        for i, v in enumerate(nums):
            self.tree[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx, val):
        i = self.n + idx
        self.tree[i] = val
        i //= 2
        while i >= 1:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def query(self, l, r):
        l += self.n; r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res += self.tree[l]; l += 1
            if not (r & 1):
                res += self.tree[r]; r -= 1
            l //= 2; r //= 2
        return res
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
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
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
public class SegmentTree {
    int n; int[] t;
    public SegmentTree(int[] a){
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
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
type SegmentTree struct {
    n    int
    tree []int
}

func NewSegmentTree(nums []int) *SegmentTree {
    n := 1
    for n < len(nums) {
        n <<= 1
    }
    
    tree := make([]int, 2*n)
    for i, v := range nums {
        tree[n+i] = v
    }
    
    for i := n - 1; i >= 1; i-- {
        tree[i] = tree[2*i] + tree[2*i+1]
    }
    
    return &SegmentTree{n: n, tree: tree}
}

func (st *SegmentTree) Update(idx, val int) {
    i := st.n + idx
    st.tree[i] = val
    i >>= 1
    
    for i >= 1 {
        st.tree[i] = st.tree[2*i] + st.tree[2*i+1]
        i >>= 1
    }
}

func (st *SegmentTree) Query(l, r int) int {
    l += st.n
    r += st.n
    res := 0
    
    for l <= r {
        if l&1 == 1 {
            res += st.tree[l]
            l++
        }
        if r&1 == 0 {
            res += st.tree[r]
            r--
        }
        l >>= 1
        r >>= 1
    }
    
    return res
}
```
</details>