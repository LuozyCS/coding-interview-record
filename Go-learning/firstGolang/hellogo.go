package main

import "fmt"

func main() {
	var a = 's'
	fmt.Printf("%T\n", a)

	const length int = 10
	fmt.Printf("%T\n", length)
}
