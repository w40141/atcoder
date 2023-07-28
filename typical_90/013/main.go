package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Load struct {
	to, distance int
}

func dijkstra(number int, matrix [100009][]Load) (distance [100009]int) {
	for i := 0; i < len(distance); i++ {
		distance[i] = 1000000000000000
	}
	distance[number] = 0

	queue := make([]int, 0)
	queue = append(queue, number)
	for len(queue) != 0 {
		pos := queue[0]
		queue = queue[1:]
		for _, m := range matrix[pos] {
			newD := distance[pos] + m.distance
			if distance[m.to] > newD {
				distance[m.to] = newD
				queue = append(queue, m.to)
			}
		}
	}
	return
}

var sc = bufio.NewScanner(os.Stdin)

func scanInt() int {
	sc.Scan()
	i, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return i
}

func main() {
	sc.Split(bufio.ScanWords)
	n, m := scanInt(), scanInt()
	var matrix [100009][]Load
	for i := 0; i < m; i++ {
		a, b, c := scanInt(), scanInt(), scanInt()
		matrix[a] = append(matrix[a], Load{b, c})
		matrix[b] = append(matrix[b], Load{a, c})
	}

	distance1 := dijkstra(1, matrix)
	distanceN := dijkstra(n, matrix)

	for i := 1; i <= n; i++ {
		fmt.Println(distance1[i] + distanceN[i])
	}
}
