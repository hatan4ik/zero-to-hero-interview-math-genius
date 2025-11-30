# Hash / Lookup — Complement Existence Theorem


### Mathematical Reasoning
**Complement Theorem:** For array S={s_i} and target t, solution exists iff ∃i,j: s_i + s_j = t ⟺ ∃i: (t - s_i) ∈ S.

**Hash Function Properties:** Using hash map H: value → index with expected O(1) lookup time. For each element x, we check membership of complement (t-x) in constant time.

**Correctness Proof:** If pair (i,j) exists with s_i + s_j = t, our algorithm will find it when processing the second element of the pair, since the first element's complement will already be stored in the hash map.

**Optimality:** Single pass through array is necessary (must examine each element at least once). Hash lookup is optimal for membership testing.

**Complexity:** Time O(n), Space O(n) for hash map storage.

### Visual Representation
```
Array: [2, 7, 11, 15], Target: 9

Step 1: Process element 2
┌─────┬─────┬─────┬─────┐
│  2  │  7  │ 11  │ 15  │
└─────┴─────┴─────┴─────┘
  ↑
  i=0

Need: 9 - 2 = 7
HashMap: {} (empty)
7 not found → Store {2: 0}

Step 2: Process element 7  
┌─────┬─────┬─────┬─────┐
│  2  │  7  │ 11  │ 15  │
└─────┴─────┴─────┴─────┘
        ↑
        i=1

Need: 9 - 7 = 2
HashMap: {2: 0}
2 found at index 0! → Return [0, 1]

🎯 Solution: indices [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
```

### Hash Table Visualization
```
Iteration 0:          Iteration 1:
┌─────────────┐      ┌─────────────┐
│ HashMap     │      │ HashMap     │
├─────────────┤      ├─────────────┤
│ (empty)     │  →   │ 2 → 0       │
└─────────────┘      │ 7 → ? (found!)│
                     └─────────────┘
```

### Algorithm Invariant
**Loop Invariant:** At iteration i, hash map contains all elements s[0...i-1] with their indices, and no valid pair exists among processed elements.

### Pseudocode
```
function twoSum(nums, target):
    seen = map()
    for i in 0..n-1:
        need = target - nums[i]
        if seen contains need: return [seen[need], i]
        seen[nums[i]] = i
    return []
```

### Trace
| i | x | need | seen | action |
|---|---|------|------|--------|
| 0 | 2 | 7    | {{}}   | store 2→0 |
| 1 | 7 | 2    | {{2→0}}| found → [0,1] |

### Narration
"Trade memory for speed; O(n) time, O(n) space. Same as cache lookup or log correlation."

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
vector<int> twoSum(vector<int>& nums, int target){
    unordered_map<int,int> seen;
    for(int i=0;i<(int)nums.size();++i){
        int need = target - nums[i];
        if(seen.contains(need)) return {seen.at(need), i};
        seen[nums[i]] = i;
    }
    return {};
}
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
import java.util.*;
public class TwoSum {
    public static int[] twoSum(int[] a, int t){
        Map<Integer,Integer> m = new HashMap<>();
        for(int i=0;i<a.length;i++){
            int need = t - a[i];
            if(m.containsKey(need)) return new int[]{m.get(need), i};
            m.put(a[i], i);
        }
        return new int[0];
    }
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)
	for i, x := range nums {
		if j, ok := seen[target-x]; ok {
			return []int{j, i}
		}
		seen[x] = i
	}
	return []int{}
}
```
</details>