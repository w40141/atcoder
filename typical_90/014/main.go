package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

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
	n := scanInt()

	var houses [100009]int
	for i := 0; i < n; i++ {
		a := scanInt()
		houses[i] = a
	}
  sort.Slice(houses[:n], func(i, j int) bool {return houses[i] > houses[j]})

	var schools [100009]int
	for i := 0; i < n; i++ {
		b := scanInt()
		schools[i] = b
	}
  sort.Slice(schools[:n], func(i, j int) bool {return schools[i] > schools[j]})

	answer := 0
	for i := 0; i < n; i++ {
		answer += int(math.Abs(float64(schools[i] - houses[i])))
	}
	fmt.Println(answer)
}
