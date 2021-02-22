package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func main() {
	sc.Split(bufio.ScanWords)
	deg := nextInt() * 10
	dis := nextInt()

	dis_n := math.Round(float64(dis) / 60 * 10) / 10
	n := 0
	switch {
	case 0 <=  dis_n && dis_n <= 0.2:
		n = 0
	case 0.3 <= dis_n && dis_n <= 1.5:
		n = 1
	case 1.6 <= dis_n && dis_n <= 3.3:
		n = 2
	case 3.4 <= dis_n && dis_n <= 5.4:
		n = 3
	case 5.5 <= dis_n && dis_n <= 7.9:
		n = 4
	case 8.0 <= dis_n && dis_n <= 10.7:
		n = 5
	case 10.8 <= dis_n && dis_n <= 13.8:
		n = 6
	case 13.9 <= dis_n && dis_n <= 17.1:
		n = 7
	case 17.2 <= dis_n && dis_n <= 20.7:
		n = 8
	case 20.8 <= dis_n && dis_n <= 24.4:
		n = 9
	case 24.5 <= dis_n && dis_n <= 28.4:
		n = 10
	case 28.5 <= dis_n && dis_n <= 32.6:
		n = 11
	default:
		n = 12
	}
	switch {
    case n == 0:
        fmt.Println("C", 0)
	case 1125 <= deg && deg< 3375:
        fmt.Println("NNE", n)
	case 3375 <= deg && deg < 5625:
        fmt.Println("NE", n)
	case 5625 <= deg && deg < 7875:
        fmt.Println("ENE", n)
	case 7875 <= deg && deg < 10125:
        fmt.Println("E", n)
	case 10125 <= deg && deg < 12375:
        fmt.Println("ESE", n)
	case 12375 <= deg && deg < 14625:
        fmt.Println("SE", n)
	case 14625 <= deg && deg < 16875:
        fmt.Println("SSE", n)
	case 16875 <= deg && deg < 19125:
        fmt.Println("S", n)
	case 19125 <= deg && deg < 21375:
        fmt.Println("SSW", n)
	case 21375 <= deg && deg < 23625:
        fmt.Println("SW", n)
	case 23625 <= deg && deg < 25875:
        fmt.Println("WSW", n)
	case 25875 <= deg && deg < 28125:
        fmt.Println("W", n)
	case 28125 <= deg && deg < 30375:
        fmt.Println("WNW", n)
	case 30375 <= deg && deg < 32625:
        fmt.Println("NW", n)
	case 32625 <= deg && deg < 34875:
        fmt.Println("NNW", n)
	default:
        fmt.Println("N", n)
	}
}
