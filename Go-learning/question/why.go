package main

import (
	"fmt"
	"time"
)

// var wg sync.WaitGroup
var ch = make(chan string, 10)

func changeValue(nums []float32) {
	fmt.Printf("2 %p\n", &nums)
	nums[0] = 1
	ch <- " "
	time.Sleep(time.Second)

}
func main() {
	slice2 := make([]float32, 3, 5) //[000]长度为3容量为5的切片
	slice2 = append(slice2, 3, 4)   //[0，0，0，1，2，3，4]

	fmt.Printf("1 %p\n", &slice2)
	fmt.Println(slice2)

	go changeValue(slice2)

	a := <-ch
	fmt.Printf("3 %p\n", &slice2)
	fmt.Println(slice2)
	fmt.Println(a)
}
