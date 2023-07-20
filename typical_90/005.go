package main

import (
	"fmt"
)

const MOD = 1000000007

func quiz1(digits, multiple int, numbers []int) int {
	dp := make([][]int, digits+1)
	for i := 0; i < digits+1; i++ {
		dp[i] = make([]int, multiple)
	}

	for _, number := range numbers {
		nex := number % multiple
		dp[1][nex] += 1
	}

	for i := 1; i < digits; i++ {
		for j := 0; j < multiple; j++ {
			for _, number := range numbers {
				nex := (10*j + number) % multiple
				dp[i+1][nex] += dp[i][j]
				dp[i+1][nex] %= MOD
			}
		}
	}
	return dp[len(dp)-1][0]
}

func quiz2(digits, multiple int, numbers []int) int {
	matrix := make([][]int, multiple)
	for i := 0; i < multiple; i++ {
		liner := make([]int, multiple)
		for j := 0; j < multiple; j++ {
			if i != j {
				liner[j] = 1
			}
		}
		matrix[i] = liner
	}
	return 0
}

func quiz3() {
}

func main() {
	var digits, multiple, ko int
	fmt.Scan(&digits, &multiple, &ko)
	numbers := make([]int, ko)
	for i := 0; i < ko; i++ {
		fmt.Scan(&numbers[i])
	}

	answer := quiz1(digits, multiple, numbers)
	fmt.Println(answer)
}
