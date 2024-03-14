package main

import (
	"fmt"
)

func main() {
	// var input string
	// fmt.Scanln(&input)

	// Split the input by space
	// values := strings.Split(input, " ")

	// // Access the two inputs
	// N, _ := strconv.Atoi(values[0])
	// V, _ := strconv.Atoi(values[1])
	var N, V int
	fmt.Scan(&V, &N)

	v := make([]int, N+1)
	w := make([]int, N+1)
	// Your code here
	for i := 1; i <= N; i++ {
		fmt.Scan(&v[i], &w[i])
	}
	f := make([][]int, N+1)
	for i := 0; i <= N; i++ {
		f[i] = make([]int, V+1)
	}

	for i := 1; i <= N; i++ {
		for j := 0; j <= V; j++ {
			f[i][j] = f[i-1][j]
			if j >= v[i] {
				// f[i][j] = math.max(f[i][j], f[i-1][j-v[i]]+w[i])
				if f[i][j] < f[i-1][j-v[i]]+w[i] {
					f[i][j] = f[i-1][j-v[i]] + w[i]
				}
			}
		}
	}
	maxValue := f[N][0]
	for _, value := range f[N] {
		if value > maxValue {
			maxValue = value
		}
	}
	fmt.Println(maxValue)

	// print(max(f[N]...))

}
