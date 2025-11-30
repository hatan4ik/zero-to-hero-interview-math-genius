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
