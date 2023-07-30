package main

import "fmt"

const MOD = 1000000007

var (
	fact    [200009]int
	factInv [200009]int
)

func power(x, y int) int {
	result := 1
	for y > 0 {
		if y&1 == 1 {
			result = result * x % MOD
		}
		x = x * x % MOD
		y >>= 1
	}
	return result
}

func modInv(x int) int {
	return power(x, MOD-2)
}

func nCr(n, r int) int {
	if r == 0 {
		return 1
	}
	if n < r || r < 0{
		return 0
	}

	nCr := fact[n] * factInv[r] % MOD * factInv[n-r] % MOD
	return nCr
}

func calc(k, n int) int {
	answer := 0
	for a := 1; a <= n/k+1; a++ {
		answer += nCr(n-(k-1)*(a-1), a)
		answer %= MOD
	}
	return answer
}

func init() {
	fact[0] = 1
	for i := 1; i < 200009; i++ {
		fact[i] = i * fact[i-1] % MOD
	}
	for i := 0; i < 200009; i++ {
		factInv[i] = modInv(fact[i])
	}
}

func main() {
	var n int
	fmt.Scan(&n)

	for k := 1; k < n; k++ {
		answer := calc(k, n)
		fmt.Println(answer)
	}
	fmt.Println(n)
}
