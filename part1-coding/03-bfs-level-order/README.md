# Tree/Graph BFS — Wavefront Propagation


### Mathematical Reasoning
**Level Function:** Define level ℓ(v) = min{edges from root to v}. BFS computes ℓ for all reachable vertices optimally.

**Wavefront Expansion:** Process vertices in non-decreasing order of distance from source. Queue maintains FIFO ordering to ensure level ℓ vertices are processed before level ℓ+1.

**Correctness Proof:** When vertex v at level ℓ is dequeued, all vertices at levels 0,1,...,ℓ-1 have been processed. Children of v are at level ℓ+1, maintaining the invariant.

**Optimality:** Each vertex and edge examined exactly once. No algorithm can do better than O(V+E) for reachability.

**Tree Specialization:** For binary trees, E = V-1, so complexity becomes O(V). Level-order traversal groups vertices by distance from root.

**Complexity:** Time O(V+E), Space O(W) where W = maximum width of any level.

### Visual Representation
```
Binary Tree:           Level-by-Level Processing:

      3               Level 0: [3]
     / \              Queue: [3] → Process 3, add children
    9   20             Result: [[3]]
   / \    \
  15  7   15          Level 1: [9, 20]  
                      Queue: [9,20] → Process 9,20, add children
                      Result: [[3], [9,20]]

                      Level 2: [15, 7, 15]
                      Queue: [15,7,15] → Process all, no children
                      Result: [[3], [9,20], [15,7,15]]
```

### BFS Wavefront Expansion
```
Step 1: Initialize     Step 2: Process Level 0    Step 3: Process Level 1
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│Queue: [3]    │    │Queue: [9,20]│    │Queue:[15,7,15]│
│Level: []    │    │Level: [3]   │    │Level: [9,20]  │
│Result: []   │    │Result:[[3]] │    │Result:[[3],   │
└─────────────┘    └─────────────┘    │        [9,20]]│
                                        └─────────────┘

Final Result: [[3], [9,20], [15,7,15]]
```

### Algorithm Invariant
**Queue Invariant:** At any point, queue contains vertices from at most two consecutive levels ℓ and ℓ+1.

### Pseudocode
```
queue=[root]; res=[]
while queue:
    level=[]
    repeat size(queue) times:
        node=pop(); append node.val
        push children if exist
    append level to res
```

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root: return []
    q,res=deque([root]),[]
    while q:
        lvl=[]
        for _ in range(len(q)):
            n=q.popleft(); lvl.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        res.append(lvl)
    return res
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
vector<vector<int>> levelOrder(Node* root){
    vector<vector<int>> res; if(!root) return res;
    queue<Node*> q; q.push(root);
    while(!q.empty()){
        int sz=q.size(); vector<int> lvl;
        for(int i=0;i<sz;++i){
            Node* n=q.front(); q.pop(); lvl.push_back(n->val);
            if(n->left) q.push(n->left);
            if(n->right) q.push(n->right);
        } res.push_back(lvl);
    } return res;
}
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
import java.util.*;
class TreeNode { int val; TreeNode left,right; TreeNode(int v){val=v;} }
public class LevelOrder {
    public static List<List<Integer>> levelOrder(TreeNode root){
        List<List<Integer>> res=new ArrayList<>();
        if(root==null) return res;
        Queue<TreeNode> q=new LinkedList<>(); q.add(root);
        while(!q.isEmpty()){
            int size=q.size(); List<Integer> lvl=new ArrayList<>();
            for(int i=0;i<size;i++){
                TreeNode n=q.poll(); lvl.add(n.val);
                if(n.left!=null) q.add(n.left);
                if(n.right!=null) q.add(n.right);
            } res.add(lvl);
        } return res;
    }
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var result [][]int
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		size := len(queue)
		var level []int

		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			level = append(level, node.Val)

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		result = append(result, level)
	}
	return result
}
```
</details>