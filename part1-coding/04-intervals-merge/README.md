# Intervals / Sorting — Measure Union


### Mathematical Reasoning
**Measure Theory:** Given intervals I₁,I₂,...,Iₙ on ℝ, compute their union ⋃Iᵢ as disjoint intervals preserving total measure.

**Sorting Lemma:** After sorting by start time, overlapping intervals appear consecutively. If intervals [a,b] and [c,d] overlap, then either a ≤ c ≤ b or c ≤ a ≤ d.

**Greedy Optimality:** Process intervals left-to-right. For current interval [s,e], either it's disjoint from previous (start new interval) or overlapping (extend previous interval to max endpoint).

**Correctness Proof:** Sorted order ensures we never miss an overlap. Greedy extension maximizes coverage at each step, producing minimal disjoint representation.

**Invariant:** Result array contains disjoint intervals in sorted order, covering all processed input intervals.

**Complexity:** Time O(n log n) for sorting + O(n) for merging = O(n log n), Space O(1) excluding output.

### Visual Representation
```
Input: [[1,3],[2,6],[8,10],[15,18]]

Step 1: Sort by start time (already sorted)
[1,3] [2,6] [8,10] [15,18]

Step 2: Process intervals one by one

Interval [1,3]:
  1───3
Result: [[1,3]]

Interval [2,6]: Overlaps with [1,3] (2 ≤ 3)
  1───3
    2─────6
  1───────6  (merged)
Result: [[1,6]]

Interval [8,10]: No overlap with [1,6] (8 > 6)
  1───────6     8──10
Result: [[1,6], [8,10]]

Interval [15,18]: No overlap with [8,10] (15 > 10)
  1───────6     8──10     15───18
Result: [[1,6], [8,10], [15,18]]
```

### Merge Process Visualization
```
Before:  [1,3] [2,6] [8,10] [15,18]
         ├─┤   ├──┤   ├─┤    ├──┤
         │ │   │  │   │ │    │  │
         1 3   2  6   8 10   15 18

After:   [1,6]       [8,10] [15,18]
         ├────┤       ├─┤    ├──┤
         │    │       │ │    │  │
         1    6       8 10   15 18

Overlap Detection:
- [1,3] and [2,6]: 2 ≤ 3 ✓ (overlap)
- [1,6] and [8,10]: 8 > 6 ✗ (no overlap)
- [8,10] and [15,18]: 15 > 10 ✗ (no overlap)
```

### Algorithm Invariant
**Merge Invariant:** At step i, result contains optimal disjoint union of intervals [0...i-1], and result[-1].end ≥ max(endpoints of merged intervals).

### Pseudocode
```
sort by start
for (s,e):
  if res empty or res[-1].end < s: push [s,e]
  else res[-1].end = max(res[-1].end, e)
```

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res=[]
    for s,e in intervals:
        if not res or res[-1][1] < s: res.append([s,e])
        else: res[-1][1] = max(res[-1][1], e)
    return res
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
vector<vector<int>> merge(vector<vector<int>>& in){
    sort(in.begin(), in.end(), [](auto&a, auto&b){ return a[0] < b[0]; });
    vector<vector<int>> res;
    for(auto &c: in){
        if(res.empty() || res.back()[1] < c[0]) res.push_back(c);
        else res.back()[1] = max(res.back()[1], c[1]);
    } return res;
}
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
import java.util.*;
public class MergeIntervals {
    public static int[][] merge(int[][] in){
        Arrays.sort(in, Comparator.comparingInt(a -> a[0]));
        List<int[]> res=new ArrayList<>();
        for(int[] cur: in){
            if(res.isEmpty() || res.get(res.size()-1)[1] < cur[0]) res.add(new int[]{cur[0],cur[1]});
            else res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1], cur[1]);
        }
        return res.toArray(new int[res.size()][]);
    }
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
import "sort"

func merge(intervals [][]int) [][]int {
	if len(intervals) == 0 {
		return [][]int{}
	}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	var result [][]int
	for _, curr := range intervals {
		if len(result) == 0 || result[len(result)-1][1] < curr[0] {
			result = append(result, curr)
		} else {
			if curr[1] > result[len(result)-1][1] {
				result[len(result)-1][1] = curr[1]
			}
		}
	}
	return result
}
```
</details>