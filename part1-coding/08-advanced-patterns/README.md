# Advanced Patterns — FAANG L5/L6 Level


### Mathematical Reasoning
**Advanced Data Structures Theory:** These patterns represent sophisticated algorithmic techniques that achieve near-optimal complexity through mathematical insights and invariant preservation.

**Amortized Analysis:** Many advanced structures use potential method or accounting method to achieve better average-case performance than worst-case bounds suggest.

**Information Theory:** Structures like tries and segment trees organize information hierarchically to minimize query complexity through divide-and-conquer principles.

## Union-Find (Disjoint Set)

### Mathematical Foundation
**Equivalence Relations:** Maintains partition of set S into disjoint equivalence classes under relation ~. Operations: find(x) returns representative, union(x,y) merges classes.

**Path Compression:** Flattens tree during find operations. Amortized analysis shows O(α(n)) per operation where α is inverse Ackermann function (effectively constant for practical n).

**Union by Rank:** Maintains tree balance by always attaching smaller tree to larger tree root, ensuring height ≤ log n.

**Complexity Analysis:**
```
α(n) - Inverse Ackermann Function:
α(1) = 1
α(4) = 2  
α(16) = 3
α(65536) = 4
α(2^65536) = 5

For all practical n: α(n) ≤ 5 (effectively constant)
```
**Complexity:** Time O(α(n)) amortized per operation, Space O(n)

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
type UnionFind struct {
	parent []int
	rank   []int
}

func NewUnionFind(n int) *UnionFind {
	parent := make([]int, n)
	rank := make([]int, n)
	for i := 0; i < n; i++ {
		parent[i] = i
	}
	return &UnionFind{parent: parent, rank: rank}
}

func (uf *UnionFind) Find(x int) int {
	if uf.parent[x] != x {
		uf.parent[x] = uf.Find(uf.parent[x]) // Path compression
	}
	return uf.parent[x]
}

func (uf *UnionFind) Union(x, y int) bool {
	px, py := uf.Find(x), uf.Find(y)
	if px == py {
		return false
	}
	if uf.rank[px] < uf.rank[py] {
		px, py = py, px
	}
	uf.parent[py] = px
	if uf.rank[px] == uf.rank[py] {
		uf.rank[px]++
	}
	return true
}
```
</details>

## Segment Tree
**See dedicated section:** [10-segment-tree-range-query](../10-segment-tree-range-query/README.md)
**Key Insight:** Range decomposition into O(log n) canonical segments for efficient queries.

## Monotonic Stack/Deque

### Mathematical Foundation
**Monotonicity Invariant:** Maintain stack/deque where elements are in monotonic order. When processing element x, remove all elements that violate monotonicity.

**Amortized Analysis:** Each element enters and exits the structure at most once, giving O(n) total complexity for n operations.

**Applications:** Next greater element, sliding window maximum, largest rectangle in histogram.

## Advanced DP Patterns

### Bitmask DP
**State Compression:** Use bitmask to represent subset states. For n items, 2ⁿ possible states.
**Complexity:** O(2ⁿ × n) typical, used for TSP, subset enumeration

### Digit DP
**Constraint Satisfaction:** Count numbers satisfying digit-based constraints without explicit enumeration.
**State:** (position, tight_bound, constraint_flags)
**Complexity:** O(log N × states)

### Tree DP
**Optimal Substructure on Trees:** Each subtree can be solved independently, then combined optimally.
**Root Selection:** Sometimes requires re-rooting technique for all-pairs problems.
**Complexity:** O(n) for most tree DP problems

### Interval DP
**Optimal Parenthesization:** Break interval [i,j] at all possible points k, solve subproblems [i,k] and [k+1,j].
**Recurrence:** dp[i][j] = min(dp[i][k] + dp[k+1][j] + cost(i,k,j))
**Complexity:** O(n³) typical

## String Algorithms

### KMP (Knuth-Morris-Pratt)
**Failure Function:** Precompute longest proper prefix which is also suffix for each position.
**No Backtracking:** Never re-examine text characters, achieving O(n+m) complexity.

### Rabin-Karp Rolling Hash
**Polynomial Hash:** h(s) = Σ s[i] × p^i mod M where p is prime, M is large prime.
**Rolling Property:** h(s[1..k]) = (h(s[0..k-1]) - s[0]) / p + s[k] × p^(k-1)
**Complexity:** O(n+m) average, O(nm) worst case

### Manacher's Algorithm
**Palindrome Centers:** Transform string to handle even/odd length palindromes uniformly.
**Linear Scan:** Use previously computed palindrome information to avoid redundant checks.
**Complexity:** O(n) time and space

### Visual Demonstrations

#### Union-Find Step-by-Step (n=6)
```
Initial: [0,1,2,3,4,5] → Union(1,2) → Union(3,4) → Union(1,3)

0 1 2 3 4 5    0 1─2 3 4 5    0 1─2 3─4 5    0    1     5
● ● ● ● ● ●    ● ●─● ● ● ●    ● ●─● ●─● ●    ●    │     ●
                                              ┌───┴───┐
                                              2       3
                                              ●       │
                                                      4
                                                      ●

Path Compression: 4→3→1 becomes 4→1 (direct)
```



### Monotonic Stack Visualization
```
Next Greater Element for [2,1,2,4,3,1]:

Step 1: Process 2    Step 2: Process 1    Step 3: Process 2
Stack: [2]           Stack: [2,1]         Stack: [2] (pop 1)
Result: [-1]         Result: [-1,-1]      Result: [-1,2,-1]

Step 4: Process 4    Step 5: Process 3    Step 6: Process 1
Stack: [4] (pop all) Stack: [4,3]         Stack: [4,3,1]
Result: [-1,2,4,-1]  Result: [-1,2,4,-1,4] Result: [-1,2,4,-1,4,-1]

Monotonic Property: Stack maintains decreasing order
```

**FAANG Applications:** Number of Islands II, Word Search II, Sliding Window Maximum, Range Sum Queries, Longest Palindromic Substring