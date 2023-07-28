package main

import (
	"fmt"
)

const LAST = 26

func main() {
	var n, k int
	var s string
	fmt.Scan(&n, &k)
	fmt.Scan(&s)

	var c [1000009][LAST]int
	for i := 0; i < LAST; i++ {
		c[n][i] = n
	}

	for i := n - 1; i >= 0; i-- {
		for j := 0; j < LAST; j++ {
			if int(s[i]-'a') == j {
				c[i][j] = i
			} else {
				c[i][j] = c[i+1][j]
			}
		}
	}

	answer := ""
	current := 0
	for i := 0; i < k; i++ {
		for j := 0; j < LAST; j++ {
			next := c[current][j]
			maxPossibleLength := n - next + i
			if maxPossibleLength >= k {
				answer += string(rune('a' + j))
				current = next + 1
				break
			}
		}
	}
	fmt.Println(answer)
}
