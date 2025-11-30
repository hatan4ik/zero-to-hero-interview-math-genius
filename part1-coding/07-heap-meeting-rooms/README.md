# Greedy / Heap — Meeting Rooms II


### Mathematical Reasoning
**Interval Scheduling Theory:** Given n intervals [sᵢ, eᵢ], find minimum number of resources (rooms) needed such that no two overlapping intervals use the same resource.

**Greedy Optimality:** Process intervals by start time. For each new interval, reuse the earliest-finishing room if possible, otherwise allocate new room. This greedy choice is optimal.

**Proof of Correctness:** 
1. **Lower Bound:** At any time t, if k intervals are active, we need ≥ k rooms
2. **Upper Bound:** Our algorithm never uses more rooms than the maximum overlap at any point
3. **Optimality:** Algorithm achieves the lower bound, hence optimal

**Heap Invariant:** Min-heap contains end times of currently active meetings. Heap size = current room count.

**Critical Insight:** We only care about the earliest ending meeting for room reuse, not which specific room. This reduces the problem to tracking minimum end times.

**Complexity:** Time O(n log n) for sorting + n heap operations, Space O(n) for heap storage.

### Visual Representation
```
Meetings: [[0,30], [5,10], [15,20]]

Timeline Visualization:
0    5    10   15   20   25   30
|──────────────────────────────| Room 1: [0,30]
     |─────|                           Room 2: [5,10]
               |─────|                 Room 3: [15,20]

Maximum overlap: 2 rooms needed (during [5,10] when Room 1 and Room 2 overlap)
```

### Min-Heap Algorithm Visualization
```
Step 1: Sort by start time
Meetings: [[0,30], [5,10], [15,20]]

Step 2: Process [0,30]
Heap: [30]  (end time of meeting in room 1)
Rooms needed: 1

Step 3: Process [5,10]
Can reuse room? 30 > 5 (No, room 1 still occupied)
Heap: [10, 30]  (add new room)
Rooms needed: 2

Step 4: Process [15,20]
Can reuse room? min(10,30) = 10 ≤ 15 (Yes, room 2 is free)
Heap: [20, 30]  (reuse room 2, update end time)
Rooms needed: 2

Final answer: 2 rooms
```

### Heap State Transitions
```
Initial:     After [0,30]:   After [5,10]:   After [15,20]:
┌───────┐    ┌───────┐     ┌───────┐     ┌───────┐
│ Heap  │    │ Heap  │     │ Heap  │     │ Heap  │
├───────┤    ├───────┤     ├───────┤     ├───────┤
│ []    │    │ [30]  │     │[10,30]│     │[20,30]│
└───────┘    └───────┘     └───────┘     └───────┘
Size: 0      Size: 1       Size: 2       Size: 2
```

### Room Reuse Logic
```
For each new meeting [start, end]:

1. Check if earliest ending room is free:
   if heap.min ≤ start:
       ✓ Reuse room (pop old end time)
   else:
       ✗ Need new room

2. Add current meeting's end time to heap

3. Heap size = current rooms needed
```

### Algorithm Invariant
**Room Invariant:** At processing interval i, heap contains end times of meetings that haven't finished yet, representing occupied rooms.

### Pseudocode
```
sort intervals by start
heap=[]
for (s,e):
  if heap and heap.min <= s: pop
  push e
return size(heap)
```

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
import heapq

def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    h=[]
    for s,e in intervals:
        if h and h[0] <= s: heapq.heappop(h)
        heapq.heappush(h,e)
    return len(h)
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
int minMeetingRooms(vector<vector<int>>& in){
    sort(in.begin(), in.end(), [](auto&a, auto&b){ return a[0] < b[0]; });
    priority_queue<int, vector<int>, greater<int>> pq;
    for(auto &m: in){
        if(!pq.empty() && pq.top() <= m[0]) pq.pop();
        pq.push(m[1]);
    }
    return (int)pq.size();
}
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
import java.util.*;
public class MeetingRoomsII {
    public static int minMeetingRooms(int[][] in){
        Arrays.sort(in,(a,b)->a[0]-b[0]);
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        for(int[] m: in){
            if(!pq.isEmpty() && pq.peek()<=m[0]) pq.poll();
            pq.add(m[1]);
        }
        return pq.size();
    }
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
import (
    "container/heap"
    "sort"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func minMeetingRooms(intervals [][]int) int {
    if len(intervals) == 0 {
        return 0
    }
    
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    
    h := &IntHeap{}
    heap.Init(h)
    
    for _, interval := range intervals {
        if h.Len() > 0 && (*h)[0] <= interval[0] {
            heap.Pop(h)
        }
        heap.Push(h, interval[1])
    }
    
    return h.Len()
}
```
</details>