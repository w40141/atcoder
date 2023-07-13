package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)
	fmt.Printf("%d", n/100+(n/10%10)+(n%10%10))
}
