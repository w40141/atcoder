package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, a, b int
	fmt.Scan((&n))

	cards := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&cards[i])
	}
	sort.Slice(cards, func(i, j int) bool { return cards[i] > cards[j] })

	for i, num := range cards {
		if i%2 == 0 {
			a += num
		} else {
			b += num
		}
	}

	fmt.Println(a - b)
}
