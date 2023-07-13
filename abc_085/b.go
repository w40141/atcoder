package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan((&n))

	cakes := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&cakes[i])
	}
	sort.Slice(cakes, func(i, j int) bool { return cakes[i] > cakes[j] })

	count := 0
	beforeCake := 1000
	for _, num := range cakes {
		if num < beforeCake {
			beforeCake = num
			count++
		}
	}
  fmt.Println(count)
}
