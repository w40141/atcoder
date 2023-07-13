package main

import "fmt"

func main() {
	var n, y int
	fmt.Scan(&n, &y)

	result := []int{-1, -1, -1}
	flag := true
	for i := 0; i <= n && flag; i++ {
		for j := 0; j <= n; j++ {
			k := n - i - j
			if k < 0 {
				break
			}
			total := 10000*i + 5000*j + 1000*k
			if total == y {
				result[0] = i
				result[1] = j
				result[2] = k
				flag = false
				break
			}
		}
	}
	fmt.Println(result[0], result[1], result[2])
}
