package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type accPoint struct {
	firstPoint  int
	secondPoint int
}

func (p accPoint) sub(a accPoint) (int, int) {
	return p.firstPoint - a.firstPoint, p.secondPoint - a.secondPoint
}

var (
	number    int
	accPoints [100009]accPoint
	quizzes   int
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
	number = scanInt()
	accPoints[0] = accPoint{0, 0}
	for i := 1; i <= number; i++ {
		class := scanInt()
		point := scanInt()
		if class == 1 {
			accPoints[i] = accPoint{accPoints[i-1].firstPoint + point, accPoints[i-1].secondPoint}
		} else {
			accPoints[i] = accPoint{accPoints[i-1].firstPoint, accPoints[i-1].secondPoint + point}
		}
	}

	quizzes = scanInt()
	for i := 0; i < quizzes; i++ {
		left := scanInt()
		right := scanInt()
		firstPoint, secondPoint := accPoints[right].sub(accPoints[left-1])
		fmt.Println(firstPoint, secondPoint)
	}
}
