package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)

	texts := []string{"dream", "dreamer", "erase", "eraser"}
	flag := true
	for len(s) > 0 && flag {
		flag = false
		for _, text := range texts {
			if strings.HasSuffix(s, text) {
				flag = true
				s = s[:len(s)-len(text)]
				break
			}
		}
	}
	if flag {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
