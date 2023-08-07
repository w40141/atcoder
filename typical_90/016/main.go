package main

import "fmt"

const MAX_COUNT = 9999

func main() {
	var n, a, b, c int
	fmt.Scan(&n)
	fmt.Scan(&a, &b, &c)

	result := MAX_COUNT + 1
	for i := 0; i <= MAX_COUNT; i++ {
		for j := 0; i+j <= result; j++ {
			e := n - a*i - b*j
			l := e % c
			k := e / c
			if e >= 0 && l == 0 && result > i+j+k{
				result = i + j + k
			}
		}
	}
	fmt.Println(result)
}
