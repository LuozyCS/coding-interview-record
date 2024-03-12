package main

import "fmt"

// 希望测试 package main 下 calc.go 中的函数，
// 要只需要新建 calc_test.go 文件，在calc_test.go中新建测试用例即可。
// go mod init calc.go
// go test
func main() {
	fmt.Println("hello")
}
