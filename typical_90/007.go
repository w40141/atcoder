package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

const INF int = 2000000000

func lowerBound(numbers []int, target int) int {
	left, right := 0, len(numbers)

	for left < right {
		mid := left + (right-left)/2
		if numbers[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}

var sc = bufio.NewScanner(os.Stdin)

func scanInt() int {
	sc.Scan()
	i, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return i
}

func main() {
	sc.Split(bufio.ScanWords)
	N := scanInt()
	pointA := make([]int, N)
	for i := 0; i < N; i++ {
		pointA[i] = scanInt()
	}

	Q := scanInt()
	pointB := make([]int, Q)
	for i := 0; i < Q; i++ {
		pointB[i] = scanInt()
	}

	sort.Slice(pointA, func(i, j int) bool {
		return pointA[i] <= pointA[j]
	})

	for _, B := range pointB {
		index := lowerBound(pointA, B)

		diff1 := INF
		diff2 := INF
		if index < N {
			diff1 = int(math.Abs(float64(pointA[index] - B)))
		}
		if index > 0 {
			diff2 = int(math.Abs(float64(pointA[index-1] - B)))
		}
		if diff1 < diff2 {
			fmt.Println(diff1)
		} else {
			fmt.Println(diff2)
		}
	}
}
