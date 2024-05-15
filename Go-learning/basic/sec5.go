package main // 这个不是很理解 好像是对文件夹要求是main？ 后面多文件再看吧
import (
	"fmt"
)

// // 5.functions
// // 5.1 参数/返回值
// // 参数可以有多个，返回值也支持有多个。
// // 特别地，package main 中的func main() 约定为可执行程序的入口。
// // 实现2个数的加法（一个返回值）和除法（多个返回值）：

//	func add(num1 int, num2 int) int {
//		return num1 + num2
//	}
//

// 也可以给返回值命名，简化 return，例如 add 函数可以改写为
// func add(num1 int, num2 int) (ans int) {
// 	ans = num1 + num2
// 	return
// }

// func div(num1 int, num2 int) (int, int) {
// 	return num1 / num2, num1 % num2
// }

// // 复习指针，如果没有返回值就不用写后面的扩号,或者int error这样的返回值
// func add_point(num int) {
// 	num += 1
// }

// func realAdd_point(num *int) {
// 	// 知道num指的是一个地址
// 	*num += 1 // *num是取地址对应的值
// }

// // 5.2错误处理 nil errors.New
// // 可以通过 errorw.New 返回自定义的错误
// func hello(name string) error {
// 	if len(name) == 0 {
// 		return errors.New("error: name is null")
// 	}
// 	fmt.Println("Hello,", name)
// 	return nil
// }

// // 5.2错误处理 panic
//	func get(index int) int {
//		arr := make([]int, 3, 4)
//		// arr = append(arr, 1, 2, 3)
//		return arr[index]
//	}

// 5.2 错误处理  defer 和 recover
// 在 get 函数中，使用 defer 定义了异常处理的函数，在协程退出前，会执行完 defer 挂载的任务。
// 因此如果触发了 panic，控制权就交给了 defer。
// 在 defer 的处理逻辑中，使用 recover，使程序恢复正常，并且将返回值设置为 -1。
// 在这里也可以不处理返回值，如果不处理返回值，返回值将被置为默认值 0。

func get(index int) (ret int) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println(r) // 输出的是：runtime error: index out of range [5] with length 3
			fmt.Println("Some error happened!", r)
			ret = -1
		}
	}()
	arr := [3]int{2, 3, 4}
	return arr[index]
}

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

	// // 5.2错误处理 error handling
	// // 如果函数实现过程中，如果出现不能处理的错误，可以返回给调用者处理。
	// // 比如我们调用标准库函数os.Open取文件，os.Open 有2个返回值，第一个是 *File，第二个是 error， 如果调用成功，error 的值是 nil，如果调用失败，例如文件不存在，我们可以通过 error 知道具体的错误信息。
	// // go编译器（还是别的插件）似乎是会自动帮你补全import
	// _, err := os.Open("filename.txt")
	// // nil 是一个预定义的标识符，用来表示指针、channel、func、interface、map、slice的零值，也就是说，这些类型的零值都是 nil。
	// if err != nil {
	// 	fmt.Println(err) // open filename.txt: no such file or directory
	// }

	// if err := hello(""); err != nil {
	// 	fmt.Println(err) // error: name is null
	// }

	// // error 往往是能预知的错误，但是也可能出现一些不可预知的错误，例如数组越界：
	// // 这种错误可能会导致程序非正常退出，在 Go 语言中称之为 panic。
	// fmt.Println(get(3)) // 我设置了数组（切片）长度是3，容量是4，但是第4位是越界的，因为不存在。
	// // index out of range [3]  get多少这里就写多少
	// fmt.Println("finish") //上面的Hello World会打印出来，但是finish不会打印出来

	// 在 Python、Java 等语言中有 try...catch 机制，在 try 中捕获各种类型的异常，在 catch 中定义异常处理的行为。
	// Go 语言也提供了类似的机制 defer 和 recover。
	fmt.Println(get(5))
	fmt.Println("finish")
}
