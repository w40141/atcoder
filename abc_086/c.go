package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Scan(&n)

	var t1, t2 int
	var x1, x2, y1, y2 float64
	flag := true
	for i := 0; i < n; i++ {
		fmt.Scan(&t2, &x2, &y2)
		t := t2 - t1
		x := math.Abs(x2 - x1)
		y := math.Abs(y2 - y1)
		d := int(x + y)
		if t < d || t%2 != d%2 {
			flag = false
			break
		}
		t1, x1, y1 = t2, x2, y2
	}
	if flag {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
