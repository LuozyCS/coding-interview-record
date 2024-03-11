package main

// 有的时候需要go mod init xxx，有的时候又不需要，不知道为什么

import "fmt"

// 6.1 结构体 方法
// 还记得之前用的 type Gender int8 吗？和这里定义结构体差不多
type Student struct {
	name string
	age  int
}

// 实现方法与实现函数的区别在于，
// func 和函数名hello 之间，加上该方法对应的实例名 stu 及其类型 *Student，可以通过实例名访问该实例的字段name和其他方法了。
func (stu *Student) hello(person string) string {
	fmt.Println(stu.age) // 内部调用是用上面定义的stu
	return fmt.Sprintf("hello %s, I am %s", person, stu.name)
}

func main() {
	fmt.Println("Hello, World!")

	// sec6 结构体 方法 接口
	// 6.1 结构体 方法
	// Golang不是面向对象语言，但是支持面向对象编程。
	// 结构体类似于其他语言中的 class，可以在结构体中定义多个字段，为结构体实现方法，实例化等。
	// 接下来我们定义一个结构体 Student，并为 Student 添加 name，age 字段，并实现 hello() 方法。

	// 使用 Student{field: value, ...}的形式创建 Student 的实例，字段不需要每个都赋值，没有显性赋值的变量将被赋予默认值，例如 age 将被赋予默认值 0。
	stu111 := Student{
		name: "Tom",
	}
	// 调用方法通过 实例名.方法名(参数) 的方式。
	msg := stu111.hello("Jack")
	fmt.Println(msg)

	// 除此之外，还可以使用 new 实例化：
	stu2 := new(Student)
	fmt.Println(stu2.hello("Alice")) // hello Alice, I am  , name 被赋予默认值""
	stu2.name = "Bill"
	fmt.Println(stu2.hello("Alice")) // hello Alice, I am Bill

}
