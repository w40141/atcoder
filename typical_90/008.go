package main

import (
	"fmt"
)

const mod int = 1000000007

func main() {
	var N int
	var S string
	fmt.Scan(&N)
	fmt.Scan(&S)
	var dp [100009][8]int
	dp[0][0] = 1

	for i := 0; i < N; i++ {
		for j := 0; j < 8; j++ {
			dp[i+1][j] += dp[i][j]
			if S[i] == 'a' && j == 0 {
				dp[i+1][j+1] += dp[i][j]
			}
			if S[i] == 't' && j == 1 {
				dp[i+1][j+1] += dp[i][j]
			}
			if S[i] == 'c' && j == 2 {
				dp[i+1][j+1] += dp[i][j]
			}
			if S[i] == 'o' && j == 3 {
				dp[i+1][j+1] += dp[i][j]
			}
			if S[i] == 'd' && j == 4 {
				dp[i+1][j+1] += dp[i][j]
			}
			if S[i] == 'e' && j == 5 {
				dp[i+1][j+1] += dp[i][j]
			}
			if S[i] == 'r' && j == 6 {
				dp[i+1][j+1] += dp[i][j]
			}
		}
		for j := 0; j < 8; j++ {
			dp[i+1][j] %= mod
		}
	}
	fmt.Println(dp[N][7])
}
