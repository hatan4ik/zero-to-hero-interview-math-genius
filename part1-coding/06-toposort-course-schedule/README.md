# Topological Sort — Partial Order Linearization


### Mathematical Reasoning
**Partial Order Theory:** Given directed acyclic graph (DAG) G=(V,E), a topological ordering is a linear arrangement of vertices such that for every edge (u,v), u appears before v.

**Existence Theorem:** A directed graph has a topological ordering if and only if it is acyclic (DAG). This follows from the fact that cycles create circular dependencies.

**Kahn's Algorithm Correctness:** 
1. **Invariant:** Vertices with indegree 0 have no unprocessed predecessors
2. **Progress:** Removing a vertex decreases indegree of successors
3. **Termination:** Either all vertices processed (valid topological order) or cycle detected

**Cycle Detection:** If |output| < |V|, then remaining vertices form strongly connected components (cycles).

**Uniqueness:** Topological ordering is unique iff the graph is a Hamiltonian path. Otherwise, multiple valid orderings exist.

**Complexity:** Time O(V+E) for building graph + processing each vertex/edge once, Space O(V+E) for adjacency list.

### Visual Representation
```
Course Prerequisites: [[1,0], [2,0], [3,1], [3,2]]
Meaning: Course 1 requires Course 0, Course 2 requires Course 0, etc.

Dependency Graph:
    0 ───┬─── 1 ─── 3
        │       │   ╱
        │       │  ╱
        └─── 2 ──┘

Indegree Count:
Node 0: indegree = 0 (no prerequisites)
Node 1: indegree = 1 (requires course 0)
Node 2: indegree = 1 (requires course 0)  
Node 3: indegree = 2 (requires courses 1 and 2)
```

### Kahn's Algorithm Step-by-Step
```
Step 1: Initialize
Queue: [0]  (nodes with indegree 0)
Indegree: [0, 1, 1, 2]
Result: []

Step 2: Process node 0
Queue: [1, 2]  (after reducing indegrees of 1,2)
Indegree: [0, 0, 0, 2]
Result: [0]

Step 3: Process node 1
Queue: [2]  (after reducing indegree of 3)
Indegree: [0, 0, 0, 1]
Result: [0, 1]

Step 4: Process node 2  
Queue: [3]  (after reducing indegree of 3)
Indegree: [0, 0, 0, 0]
Result: [0, 1, 2]

Step 5: Process node 3
Queue: []  (no more nodes)
Indegree: [0, 0, 0, 0]
Result: [0, 1, 2, 3]

Valid topological order: 0 → 1 → 2 → 3
```

### Cycle Detection Visualization
```
No Cycle (DAG):           With Cycle:
    A ─── B                A ─── B
    │   │                │   │
    │   │                │   │
    C ─── D                C ─── D
                              │   │
                              └───┘

Result: All nodes         Result: Some nodes
        processed                 remain unprocessed
        (valid topo sort)         (cycle detected)
```

### Algorithm Invariant
**Queue Invariant:** At any point, queue contains exactly the vertices with current indegree 0 (no unprocessed dependencies).

### Pseudocode
```
build graph + indegree
queue = nodes with indeg 0
while queue:
  u=pop; append u
  for v in adj[u]: indeg[v]--; if indeg[v]==0 push v
if len(order)==n ok else cycle
```

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
from collections import defaultdict, deque
from typing import List, Optional

def topo_sort(n: int, edges: List[List[int]]) -> Optional[List[int]]:
    g=defaultdict(list); indeg=[0 for _ in range(n)]
    for a,b in edges: g[b].append(a); indeg[a]+=1
    q=deque([i for i in range(n) if indeg[i]==0]); order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return order if len(order) == n else None
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
vector<int> topoSort(int n, vector<vector<int>>& edges){
    vector<vector<int>> g(n); vector<int> indeg(n);
    for(auto &e: edges){ g[e[1]].push_back(e[0]); indeg[e[0]]++; }
    queue<int> q; 
    for(int i=0;i<n;i++) if(indeg[i]==0) q.push(i);
    vector<int> ord;
    while(!q.empty()){
        int u=q.front(); q.pop(); ord.push_back(u);
        for(int v: g[u]) if(--indeg[v]==0) q.push(v);
    }
    return (int)ord.size()==n?ord:vector<int>{};
}
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
import java.util.*;
import java.util.stream.IntStream;

public class TopoSort {
    public static int[] topoSort(int n, int[][] edges){
        List<List<Integer>> g=new ArrayList<>();
        for(int i=0;i<n;i++) g.add(new ArrayList<>());
        int[] indeg=new int[n];
        for(int[] e: edges){ g.get(e[1]).add(e[0]); indeg[e[0]]++; }
        Queue<Integer> q = new LinkedList<>();
        IntStream.range(0, n).filter(i -> indeg[i] == 0).forEach(q::add);
        int[] order=new int[n]; int k=0;
        while(!q.isEmpty()){
            int u=q.poll(); order[k++]=u;
            for(int v: g.get(u)) if(--indeg[v]==0) q.add(v);
        }
        return k==n?order:new int[0];
    }
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
func topoSort(n int, edges [][]int) []int {
    graph := make([][]int, n)
    indegree := make([]int, n)
    
    for _, edge := range edges {
        graph[edge[1]] = append(graph[edge[1]], edge[0])
        indegree[edge[0]]++
    }
    
    var queue []int
    for i := 0; i < n; i++ {
        if indegree[i] == 0 {
            queue = append(queue, i)
        }
    }
    
    var result []int
    for len(queue) > 0 {
        u := queue[0]
        queue = queue[1:]
        result = append(result, u)
        
        for _, v := range graph[u] {
            indegree[v]--
            if indegree[v] == 0 {
                queue = append(queue, v)
            }
        }
    }
    
    if len(result) == n {
        return result
    }
    return []int{}
}
```
</details>