package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type task struct {
	deadline int
	required int
	reword   int
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

func judge2(tasks []task) int {
	answer := 0
	for mask := 0; mask < (1 << len(tasks)); mask++ {
		nowTime := 0
		nowMoney := 0
		for i, task := range tasks {
			if mask&(1<<i) == 0 {
				continue
			}
			if nowTime+task.required > task.deadline {
				nowMoney = 0
				break
			}
			nowTime += task.required
			nowMoney += task.reword
		}
		if answer < nowMoney {
			answer = nowMoney
		}
	}
	return answer
}

func judge3(tasks []task) int {
	// dp[doneTask][sumTime]
	var dp [5009][5009]int
	for i, task := range tasks {
		for j := 0; j <= 5000; j++ {
			if dp[i+1][j] < dp[i][j] {
				dp[i+1][j] = dp[i][j]
			}
			time := j + task.required
			if time <= task.deadline {
        money := dp[i][j] + task.reword
				if dp[i+1][time] < money {
					dp[i+1][time] = money
				}
			}
		}
	}
  answer := 0
  for i := 0; i <= 5000; i++ {
    if dp[len(tasks)][i] > answer {
      answer = dp[len(tasks)][i]
    }
  }
	return answer
}

func main() {
	sc.Split(bufio.ScanWords)
	n := scanInt()
	tasks := make([]task, n)
	for i := 0; i < n; i++ {
		tasks[i] = task{
			scanInt(),
			scanInt(),
			scanInt(),
		}
	}

	sort.Slice(tasks, func(i, j int) bool {
		return tasks[i].deadline < tasks[j].deadline
	})

	answer := judge3(tasks)
	fmt.Println(answer)
}
