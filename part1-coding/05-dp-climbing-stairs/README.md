# Dynamic Programming — Linear Recurrence


### Mathematical Reasoning
**Recurrence Relation:** f(n) = f(n-1) + f(n-2) with base cases f(1)=1, f(2)=2. This is the Fibonacci sequence shifted by one index.

**Principle of Optimality:** To reach step n, we must come from either step n-1 (taking 1 step) or step n-2 (taking 2 steps). The number of ways is the sum of ways to reach these predecessor states.

**Mathematical Induction:** 
- Base: f(1)=1, f(2)=2 ✓
- Hypothesis: f(k) is correct for all k < n
- Step: f(n) = f(n-1) + f(n-2) by definition of the problem

**Closed Form Solution:** f(n) = (φⁿ⁺¹ - ψⁿ⁺¹)/√5 where φ = (1+√5)/2 (golden ratio), ψ = (1-√5)/2.

**Space Optimization:** Since f(n) only depends on previous two values, we can use O(1) space with rolling variables instead of O(n) array.

**Complexity:** Time O(n), Space O(1) with rolling technique.

### Visual Representation
```
Climbing Stairs (n=5): How many ways to reach step 5?

Staircase Visualization:
     ┌───┐ 5
   ┌─┤   │
 ┌─┤ │   │
┌┤ │ │   │
││ │ │   │
││ │ │   │
││ │ │   │
─1 2 3 4   5

Recurrence Relation: f(n) = f(n-1) + f(n-2)

Step-by-step calculation:
f(1) = 1  (base case: 1 way to reach step 1)
f(2) = 2  (base case: 2 ways to reach step 2)
f(3) = f(2) + f(1) = 2 + 1 = 3
f(4) = f(3) + f(2) = 3 + 2 = 5  
f(5) = f(4) + f(3) = 5 + 3 = 8
```

### Fibonacci Pattern Visualization
```
Step:  1  2  3  4  5  6  7  8 ...
Ways:  1  2  3  5  8 13 21 34 ...
       │  │  │  │  │  │  │  │
       └──┴──┴──┴──┴──┴──┴──┴── Fibonacci sequence!
          3  5  8 13 21 34 55

Rolling Variables (Space Optimization):
Iteration 3: a=1, b=2 → c=1+2=3, a=2, b=3
Iteration 4: a=2, b=3 → c=2+3=5, a=3, b=5
Iteration 5: a=3, b=5 → c=3+5=8, a=5, b=8

Result: f(5) = 8 ways
```

### Ways to Reach Each Step
```
Step 1: • (1 way)
        1-step

Step 2: •• (2 ways)
        1-step + 1-step
        2-step

Step 3: ••• (3 ways)
        1+1+1
        1+2
        2+1

Step 4: •••• (5 ways)
        1+1+1+1
        1+1+2
        1+2+1  
        2+1+1
        2+2
```

### Algorithm Invariant
**Loop Invariant:** At iteration i, variables a and b contain f(i-1) and f(i) respectively.

### Pseudocode
```
if n<=2: return n
a=1; b=2
for i in 3..n: c=a+b; a=b; b=c
return b
```

<details>
<summary><strong>🐍 Python Implementation</strong></summary>

```python
def climb_stairs(n:int)->int:
    if n<=2: return n
    a,b=1,2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b
```
</details>

<details>
<summary><strong>⚡ C++ Implementation</strong></summary>

```cpp
int climbStairs(int n){
    if(n<=2) return n; int a=1,b=2;
    for(int i=3;i<=n;i++){ int c=a+b; a=b; b=c; } return b;
}
```
</details>

<details>
<summary><strong>☕ Java Implementation</strong></summary>

```java
public class ClimbStairs {
    public static int climbStairs(int n){
        if(n<=2) return n;
        int a=1,b=2;
        for(int i=3;i<=n;i++){ int c=a+b; a=b; b=c; }
        return b;
    }
}
```
</details>

<details>
<summary><strong>🚀 Go Implementation</strong></summary>

```go
func climbStairs(n int) int {
    if n <= 2 {
        return n
    }
    a, b := 1, 2
    for i := 3; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}
```
</details>