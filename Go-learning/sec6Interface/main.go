package main

import "fmt"

// Go 语言中，并不需要显式地声明实现了哪一个接口，只需要直接实现该接口对应的方法即可。
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

func (stu *Student) getAge() int {
	return stu.age
}

type Worker struct {
	name   string
	gender string
}

func (w *Worker) getName() string {
	return w.name
}

func (w *Worker) getGender() string {
	return w.gender
}

func main() {

	// 6.2 接口
	// 一般而言，接口定义了一组方法的集合，接口不能被实例化，一个类型可以实现多个接口。
	// 举一个简单的例子，定义一个接口 Person和对应的方法 getName() 和 getAge()：

	// 实例化 Student后，强制类型转换为接口类型 Person。
	// 在Go语言中，接口类型的变量可以存储两种类型的值：
	// 一种是实现了该接口的值的类型，另一种是实现了该接口的指针类型。
	// 在这个例子中，Student结构体实现了Person接口，但是getName方法使用的是指针接收者，所以需要取Student的地址。
	// 如果getName方法使用的是值接收者，那么可以直接将Student的值赋给Person类型的变量。
	var p Person = &Student{
		name: "Tom",
		age:  18,
	}

	fmt.Println(p.getName()) // Tom

	// 在上面的例子中，我们在 main 函数中尝试将 Student 实例类型转换为 Person。
	// 如果 Student 没有完全实现 Person 的方法，比如我们将 (*Student).getName() 删掉，编译时会出现如下报错信息。
	// *Student does not implement Person (missing getName method)
	// 但是删除 (*Worker).getName() 程序并不会报错，因为我们并没有在 main 函数中使用。
	// 这种情况下我们如何确保某个类型实现了某个接口的所有方法呢？
	// 一般可以使用下面的方法进行检测，如果实现不完整，编译期将会报错。
	var _ Person = (*Student)(nil) // 在 Go 语言中，你不能直接将 nil 转换为一个具体的类型，除非这个类型是一个接口类型或者指针类型。因此不能写（Student）（nil）
	var _ Person = (*Worker)(nil)
	// 解释：将空值 nil 转换为 *Student 类型，再转换为 Person 接口，如果转换失败，说明 Student 并没有实现 Person 接口的所有方法。

	// 实例可以强制类型转换为接口，接口也可以强制类型转换为实例。
	stu := p.(*Student) // 接口转为实例
	// 解释：p是接口变量，它持有一个 *Student 类型的值。
	// p.(*Student) 就是在断言 p 的动态值是否是 *Student 类型。如果 p 的动态值确实是 *Student 类型，那么这个类型断言就会成功，stu 就会是 p 的动态值，类型为 *Student。
	fmt.Println(stu.getAge())

	// worker := p.(*Worker) // 这里会报错，因为p持有的是 *Student 类型的值，而不是 *Worker 类型的值
	// fmt.Println(worker.getGender())

	// 6.3 空接口
	// 如果定义了一个没有任何方法的空接口，那么这个接口可以表示任意类型。
	m := make(map[string]interface{}) // 字典，方括号里是key，右边是value。
	m["name"] = "Tom"
	m["age"] = 18
	m["scores"] = [3]int{98, 99, 85}
	fmt.Println(m) // map[age:18 name:Tom scores:[98 99 85]]

	// 回顾一下之前的字典，可以看到m1和m2都是固定了key和value的类型，而m是可以存储任意类型的。
	// 这就是空接口的好处。和python一样灵活的字典。
	// m1 := make(map[string]int)
	// m2 := map[string]string{
	// 	"Sam": "Male",
	// 	"Alice": "Female",
	// }
}
