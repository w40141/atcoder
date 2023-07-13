package main

import "fmt"

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)
	c := a * b
	if c%2 == 0 {
		fmt.Printf("Even")
	} else {
		fmt.Printf("Odd")
	}
}
