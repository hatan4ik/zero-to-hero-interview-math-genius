package main

func topoSort(n int, edges [][]int) []int {
	graph := make([][]int, n)
	indegree := make([]int, n)

	for _, edge := range edges {
		graph[edge[1]] = append(graph[edge[1]], edge[0])
		indegree[edge[0]]++
	}

	var queue []int
	for i := 0; i < n; i++ {
		if indegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	var result []int
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		result = append(result, u)

		for _, v := range graph[u] {
			indegree[v]--
			if indegree[v] == 0 {
				queue = append(queue, v)
			}
		}
	}

	if len(result) == n {
		return result
	}
	return []int{}
}