# Sliding Window — Moving-Integral Invariant


### Mathematical Reasoning
**Invariant Preservation:** Maintain window W=[L,R) such that ∀i,j ∈ W: s[i] ≠ s[j] (no duplicates).

**Amortized Analysis:** Each character enters the window exactly once (when R advances) and exits at most once (when L advances). Since L is monotonically non-decreasing and bounded by R, total operations = O(n).

**Optimality Proof:** For any position R, the maximum valid window ending at R is unique and determined by the rightmost occurrence of s[R] before position R. Our algorithm finds this optimally by maintaining the invariant.

**Complexity:** Time O(n), Space O(min(m,n)) where m = alphabet size.

### Visual Representation
```
String: "abcabcbb"
Step-by-step sliding window expansion:

Step 1: a|bcabcbb     Window=[0,1), Set={a}, Length=1
        L R

Step 2: ab|cabcbb     Window=[0,2), Set={a,b}, Length=2  
        L  R

Step 3: abc|abcbb     Window=[0,3), Set={a,b,c}, Length=3
        L   R

Step 4: abc|a|bcbb    Duplicate 'a' found! Shrink window
        L   R         Remove 'a' from set, L moves right

Step 5:  bc|a|bcbb    Window=[1,4), Set={b,c,a}, Length=3
         L   R

Step 6:  bca|b|cbb    Duplicate 'b' found! Shrink window  
         L   R        Remove 'b','c' from set, L moves right

Step 7:    a|b|cbb    Window=[3,5), Set={a,b}, Length=2
           L R

Maximum window length achieved: 3
```

### Algorithm Invariant
**Loop Invariant:** At iteration R, window [L,R) contains no duplicate characters, and L is the minimum index such that [L,R] would be valid.

### Pseudocode
```
left=0; best=0; set=∅
for right in 0..n-1:
    while s[right] in set:
        remove s[left]; left++
    add s[right]; best=max(best, right-left+1)
return best
```

### Trace ("abba")
| r | ch | L | set_before | action                 | best |
|---|----|---|------------|------------------------|------|
| 0 | a  | 0 | {{}}         | add a                  | 1    |
| 1 | b  | 0 | {{a}}        | add b                  | 2    |
| 2 | b  | 0 | {{a,b}}      | remove a,b; add b      | 2    |
| 3 | a  | 2 | {{b}}        | add a                  | 2    |

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
def longest_unique(s: str) -> int:
    seen, L, best = set(), 0, 0
    for R, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[L]); L += 1
        seen.add(ch)
        best = max(best, R - L + 1)
    return best
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
int lengthOfLongestSubstring(string s){
    unordered_set<char> st; int l=0,b=0;
    for(int r=0;r<(int)s.size();++r){
        while(st.count(s[r])) st.erase(s[l++]);
        st.insert(s[r]); b=max(b, r-l+1);
    }
    return b;
}
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
import java.util.*;
public class LongestSubstring {
    public static int lengthOfLongestSubstring(String s){
        Set<Character> set = new HashSet<>();
        int l=0,b=0;
        for(int r=0;r<s.length();r++){
            while(set.contains(s.charAt(r))) set.remove(s.charAt(l++));
            set.add(s.charAt(r));
            b = Math.max(b, r-l+1);
        }
        return b;
    }
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
func lengthOfLongestSubstring(s string) int {
    seen := make(map[byte]bool)
    l, best := 0, 0
    for r := 0; r < len(s); r++ {
        for seen[s[r]] {
            delete(seen, s[l])
            l++
        }
        seen[s[r]] = true
        if r-l+1 > best {
            best = r - l + 1
        }
    }
    return best
}
```
</details>