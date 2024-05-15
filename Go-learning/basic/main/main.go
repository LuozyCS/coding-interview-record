package main

import "fmt"

// 希望测试 package main 下 calc.go 中的函数，
// 要只需要新建 calc_test.go 文件，在calc_test.go中新建测试用例即可。
// go mod init calc.go
// go test
// 而且好像必须把文件夹名字改为main
//
// GPT：
//
//	文件夹的名字并不需要和包名相同。
//	实际上，你可以将你的 Go 代码文件放在任何你想放的地方。
//	然而，按照 Go 的最佳实践，通常我们会将同一个包的所有文件放在同一个文件夹下，并且这个文件夹的名字和包名相同。
//	这样做可以帮助我们更好地组织代码，但这并不是强制的。
func main() {
	fmt.Println("hello")
}
