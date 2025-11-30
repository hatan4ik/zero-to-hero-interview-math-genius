package main

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