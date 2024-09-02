package main

import "fmt"

func cal(i int) {
	fmt.Println("cal", i)
}
func main() {
	for i := 0; i < 10; i++ {
		go cal(i)
	}
}
