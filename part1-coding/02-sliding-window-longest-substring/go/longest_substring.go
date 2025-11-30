package main

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