// Package main provides ...
package main

import (
	"fmt"
)

func main() {
	var s, t int
	fmt.Scan(&s)
	fmt.Scan(&t)
	n := s - t
	fmt.Println(n)
}
