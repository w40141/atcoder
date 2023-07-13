package main

import "fmt"

func sumOfEach(n int) int {
	s := 0
	for n > 0 {
		s += n % 10
		n /= 10
	}
	return s
}

func main() {
	var n, a, b int
	fmt.Scan(&n, &a, &b)

	count := 0
	for i := 1; i <= n; i++ {
		c := sumOfEach(i)
		if c >= a && c <= b {
			count += i
		}
	}
	fmt.Println(count)
}
