package main

import "fmt"

type Person interface {
	getName() string
}

type Student struct {
	name string
	age  int
}

func (stu *Student) getName() string {
	return stu.name
}

type Worker struct {
	name   string
	gender string
}

func (w *Worker) getName() string {
	return w.name
}

func main() {

	// 6.2 接口
	// 一般而言，接口定义了一组方法的集合，接口不能被实例化，一个类型可以实现多个接口。
	// 举一个简单的例子，定义一个接口 Person和对应的方法 getName() 和 getAge()：

	var p Person = &Student{
		name: "Tom",
		age:  18,
	}

	fmt.Println(p.getName()) // Tom
}
