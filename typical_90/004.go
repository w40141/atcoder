package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n, w int
	var matrix [2000][2000]int
	var rows [2000]int
	var columns [2000]int

	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	fmt.Scan(&n, &w)
	for i := 0; i < n; i++ {
		for j := 0; j < w; j++ {
			sc.Scan()
			value, _ := strconv.Atoi(sc.Text())
			matrix[i][j] = value
			rows[i] += value
			columns[j] += value
		}
	}

	wtr := bufio.NewWriter(os.Stdout)
	for i := 0; i < n; i++ {
		for j := 0; j < w; j++ {
			fmt.Fprint(wtr, rows[i]+columns[j]-matrix[i][j], " ")
		}
		fmt.Fprintln(wtr)
	}
	_ = wtr.Flush()
}
