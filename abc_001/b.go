// Package main provides ...
package main

import (
	"fmt"
	"strconv"
)

func main() {
    var a int
    fmt.Scan(&a)

    m := ""
    switch {
    case a < 100:
        m = "00"
    case 100 <= a && a < 1000:
        m = "0" + strconv.Itoa(a/100)
    case 1000 <= a && a <= 5000:
        m = strconv.Itoa(a/100)
    case 6000 <= a && a <= 30000:
        m =strconv.Itoa(a/1000 + 50)
    case 35000 <= a && a <= 70000:
        m =strconv.Itoa(int(a/1000 - 30) / 5 + 80)
    default:
        m = "89"
    }
    fmt.Println(m)
}
