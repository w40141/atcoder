package main

import (
	"bufio"
	"fmt"
	"os"
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

var (
	matrix [2009][2009]bool
	h, w   int
)

type UnionFindTree struct {
	par []int
}

func initUFT(sz int) UnionFindTree {
	a := make([]int, sz)
	for i := 0; i < sz; i++ {
		a[i] = -1
	}
	return UnionFindTree{a}
}

func (u UnionFindTree) root(pos int) int {
	if u.par[pos] == -1 {
		return pos
	}
	u.par[pos] = u.root(u.par[pos])
	return u.par[pos]
}

func (u UnionFindTree) unite(a, b int) {
	s := u.root(a)
	t := u.root(b)
	if s == t {
		return
	}
	u.par[s] = t
}

func (u UnionFindTree) same(a, b int) bool {
	return u.root(a) == u.root(b)
}

func (u UnionFindTree) query1(x, y int) {
	d := [4][2]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	for _, di := range d {
		sx := x + di[0]
		sy := y + di[1]
		if !matrix[sx][sy] {
			continue
		}
		pos1 := (x-1)*w + (y - 1)
		pos2 := (sx-1)*w + (sy - 1)
		u.unite(pos1, pos2)
	}
	matrix[x][y] = true
}

func (u UnionFindTree) query2(ra, ca, rb, cb int) bool {
	if matrix[ra][ca] == false || matrix[rb][cb] == false {
		return false
	}
	pos1 := (ra-1)*w + (ca - 1)
	pos2 := (rb-1)*w + (cb - 1)
	if u.same(pos1, pos2) {
		return true
	}
	return false
}

func main() {
	sc.Split(bufio.ScanWords)
	h, w = scanInt(), scanInt()
	tree := initUFT(h * w)
	queries := scanInt()
	for i := 0; i < queries; i++ {
		t := scanInt()
		if t == 1 {
			x, y := scanInt(), scanInt()
			tree.query1(x, y)
		} else {
			ra, ca, rb, cb := scanInt(), scanInt(), scanInt(), scanInt()
			answer := tree.query2(ra, ca, rb, cb)
			if answer {
				fmt.Println("Yes")
			} else {
				fmt.Println("No")
			}
		}
	}
}
