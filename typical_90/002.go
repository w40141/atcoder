package main

import (
	"errors"
	"fmt"
)

func stackRun(maxN, num int) (string, error) {
	parens := ""
	stack := 0
	for i := maxN - 1; 0 <= i; i-- {
		point := num & (1 << i)
		if stack < 0 {
			return "", errors.New("")
		}
		if point == 0 {
			stack++
			parens += "("
		} else {
			stack--
			parens += ")"
		}
	}
	if stack == 0 {
		return parens, nil
	}
	return "", errors.New("")
}

func main() {
	var n int
	fmt.Scan(&n)
	if n%2 != 1 {
		for i := 0; i < (1 << n); i++ {
			p, e := stackRun(n, i)
			if e == nil {
				fmt.Println(p)
			}
		}
	}
}
