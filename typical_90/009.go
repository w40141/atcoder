package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

var (
	points [2009]Point
	N      int
)

type Point struct {
	x, y int
}

var sc = bufio.NewScanner(os.Stdin)

func lowerBound(numbers []float64, target float64) int {
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

func scanInt() int {
	sc.Scan()
	i, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return i
}

func (p Point) Angle() float64 {
	angle := math.Atan2(float64(p.y), float64(p.x))
	degree := angle * 180 / math.Pi
	if degree < 0 {
		degree += 360
	}
	return degree
}

func tangle(a, c float64) float64 {
	b := math.Abs(a - c)
	if b > 180.0 {
		b = 360 - b
	}
	return b
}

func (p Point) getNewPosition(a Point) Point {
	return Point{p.x - a.x, p.y - a.y}
}

func searchCenter(posB int, point Point) float64 {
	var arguments []float64
	for i := 0; i < N; i++ {
		if i == posB {
			continue
		}
		newPoint := point.getNewPosition(points[i])
		argument := newPoint.Angle()
		arguments = append(arguments, argument)
	}
	sort.Slice(arguments, func(i, j int) bool { return arguments[i] < arguments[j] })

	answer := 0.0
	for _, arg := range arguments {
		target := arg + 180.0
		if target > 360.0 {
			target -= 360.0
		}
		pos := lowerBound(arguments, target)
		index1 := pos % len(arguments)
		index2 := (pos + len(arguments) - 1) % len(arguments)
		b1 := tangle(arg, arguments[index1])
		b2 := tangle(arg, arguments[index2])
		if b1 > b2 {
			if b1 > answer {
				answer = b1
			}
		} else {
			if b2 > answer {
				answer = b2
			}
		}
	}

	return answer
}

func solve() float64 {
	answer := 0.0
	for i, point := range points {
		if i >= N {
			break
		}
		result := searchCenter(i, point)
		if result > answer {
			answer = result
		}
	}
	return answer
}

func main() {
	sc.Split(bufio.ScanWords)
	N = scanInt()
	for i := 0; i < N; i++ {
		points[i] = Point{scanInt(), scanInt()}
	}

	answer := solve()
	fmt.Print(answer)
}
