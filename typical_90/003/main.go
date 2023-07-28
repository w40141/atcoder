package main

import (
	"fmt"
)

func findMax(numbers []int) (int, int) {
	var index, value int
	for i, num := range numbers {
		if num > value {
			index = i
			value = num
		}
	}
	return index, value
}

func getDist(n, start int, graph [][]int) []int {
	dist := make([]int, n+1)
	visited := make([]int, n+1)
	willVisit := []int{start}
	for len(willVisit) > 0 {
		target := willVisit[0]
		willVisit = willVisit[1:]
		for _, m := range graph[target] {
			if visited[m] == 1 {
				continue
			}
			dist[m] = dist[target] + 1
			willVisit = append(willVisit, m)
		}
		visited[target] = 1
	}
	return dist
}

func main() {
	var a, b, n int
	fmt.Scan(&n)
	graph := make([][]int, n+1)
	for i := 0; i < n-1; i++ {
		fmt.Scan(&a, &b)
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	dist := getDist(n, 1, graph)
	index, _ := findMax(dist)
	dist = getDist(n, index, graph)
	_, value := findMax(dist)
	fmt.Println(value + 1)
}
