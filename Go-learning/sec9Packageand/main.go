package main

import "fmt"

// 一般来说，一个文件夹可以作为 package，同一个 package 内部变量、类型、方法等定义可以相互看到。
// 比如我们新建一个文件 calc.go， main.go 平级，分别定义 add 和 main 方法。
func main() {
	fmt.Println(add(1, 2))
	// 需要运行go run .，而不是 go run main.go
	// 因为go run main.go只编译main.go，而add方法在calc.go中

	// Go 语言也有 Public 和 Private 的概念，粒度是包。
	// 如果类型/接口/方法/函数/字段的首字母大写，则是 Public 的，对其他 package 可见，如果首字母小写，则是 Private 的，对其他 package 不可见。
}
