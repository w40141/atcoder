package main

import (
	"fmt"
	"math"
)

func solve(n int) bool {
	return false
}

func main() {
	var n, l, k int
	fmt.Scan(&n, &l, &k)

	array := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&array[i])
	}

  // ok: 範囲内の最大値、ng: 範囲外の最大値
	ok := l
	ng := -1
  // 大きさを考慮しないため
	for math.Abs(float64(ok-ng)) > 1 {
		mid := (ok + ng) / 2

    // 切った個数、切ったところの長さ
		var cnt, pre int
		for i := 0; i < n; i++ {
      // 切ったときの長さ、残りの長さ
			if array[i]-pre >= mid && l-array[i] >= mid {
				cnt++
				pre = array[i]
			}
		}

    // 切った個数が満たす場合
		if cnt >= k {
			ng = mid
		} else {
			ok = mid
		}
	}
	fmt.Print(ng)
}
