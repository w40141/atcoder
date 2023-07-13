package main

import (
	"fmt"
)

func main() {
	result := 100000000
	var arraySize int
	fmt.Scanln(&arraySize)
	var number int

	for i := 0; i < arraySize; i++ {
		count := 0
		fmt.Scan(&number)
		for number%2 == 0 {
			number /= 2
			count++
		}
		if count < result {
			result = count
		}
	}
	fmt.Println(result)
}
