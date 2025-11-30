def longest_unique(s: str) -> int:
    seen, L, best = set(), 0, 0
    for R, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[L]); L += 1
        seen.add(ch)
        best = max(best, R - L + 1)
    return best
