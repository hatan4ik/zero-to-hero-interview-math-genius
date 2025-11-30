package main

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