package main // 这个不是很理解 好像是对文件夹要求是main？ 后面多文件再看吧
import "fmt"

// // 5.functions
// // 5.1 参数/返回值
// // 参数可以有多个，返回值也支持有多个。
// // 特别地，package main 中的func main() 约定为可执行程序的入口。
// // 实现2个数的加法（一个返回值）和除法（多个返回值）：

// func add(num1 int, num2 int) int {
// 	return num1 + num2
// }

// func div(num1 int, num2 int) (int, int) {
// 	return num1 / num2, num1 % num2
// }

// // 复习指针
// func add_point(num int) {
// 	num += 1
// }

// func realAdd_point(num *int) {
// 	// 知道num指的是一个地址
// 	*num += 1 // *num是取地址对应的值
// }

func main() {
	fmt.Println("Hello, World!")

	// // 5.1 参数/返回值
	// quo, rem := div(100, 17)
	// fmt.Println(quo, rem)     // 5 15 除数和余数
	// fmt.Println(add(100, 17)) // 117

	// // 指针复习
	// num := 100
	// add_point(num)
	// fmt.Println(num) // 100 传值

	// realAdd_point(&num) // 取num的地址进函数
	// fmt.Println(num)    // 101 传指针

	// // 另外 我尝试过如果传入&num但是func定义用int接收，这样编译器是不允许的。

	// 5.2错误处理 error handling

}
