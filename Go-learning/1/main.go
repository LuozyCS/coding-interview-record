package main
import "fmt"
// import "reflect"

/*
//或者可以这么写
import (
	"fmt"
	"reflect"
)
*/
func main(){
	// /*
	// 	注释
	// */
	// fmt.Println("Hello, World!")
	// // 无法重复声明
	// // a := 1
	// // fmt.Println(a)
	// var a = 1
	// fmt.Println(a)

	// // var a = 2.2
	// // fmt.Println(a)
	// var a int8 = 10
	// var c1 byte = 'a'
	// var b float32 = 12.2
	// var msg = "Hello World" //这个是string类型
	// ok := false

	// str1 := "Golang"
    // str2 := "Go语言"
    // fmt.Println(reflect.TypeOf(str2[2]).Kind()) // uint8
    // fmt.Println(str1[2], string(str1[2]))       // 108 l
    // fmt.Printf("%d %c\n", str2[2], str2[2])     // 232 è
    // fmt.Println("len(str2)：", len(str2))       // len(str2)： 8
	// 啊因为字符串是以 byte 数组的形式存储的，所以，str2[2] 的值并不等于语。
	// str2 的长度 len(str2) 也不是 4，而是 8（ Go 占 2 byte，语言占 6 byte）。、
	
	// 正确的处理方式是将 string 转为 rune 数组：
	// 转换成 []rune 类型后，字符串中的每个字符，
	// 无论占多少个字节都用 int32 来表示，因而可以正确处理中文。

	// str2 := "Go语言"
	// runeArr := []rune(str2)
	// fmt.Println(reflect.TypeOf(runeArr[2]).Kind()) // int32
	// fmt.Println(runeArr[2], string(runeArr[2]))    // 35821 语
	// fmt.Println(runeArr[1], string(runeArr[1]))    // 111  o
	// fmt.Println("len(runeArr):", len(runeArr))    // len(runeArr)： 4


	// 数组
	// var arr1 [5][5]int
	// var arr1 [5][5] int
	// fmt.Println(arr1)

	// var arr = [5]int{1, 2, 3, 4, 5}
	// // 或 arr := [5]int{1, 2, 3, 4, 5}
	// for i:=0; i<5; i++{
	// 	arr[i] ++
	// 	arr[i] += 100
	// }
	// fmt.Println(arr)

	// var arr9 = [5]int{1,2}
	// fmt.Println(arr9)
	// // 不定长数组
	// marray := [...]{1,2,3,4,5}
	// 可以看到数组与切片的创建形式完全不同。
	// 数组操作比较麻烦，数组长度无法改变，所以一般用切片
	// 片是数组的抽象。 
	// 切片使用数组作为底层结构。
	// 切片包含三个组件：容量，长度和指向底层数组的指针,切片可以随时进行扩展

	// 声明切片
	// slice1 := make([]float32, 0) // 长度为0的切片
	// fmt.Println(len(slice1), cap(slice1)) // 0 0 为设定初始容量，容量为0
	// slice2 := make([]float32, 3, 5) // [0 0 0] 长度为3容量为5的切片
	// fmt.Println(len(slice2), cap(slice2)) // 3 5
	// // 长度为3的意思是默认初始化了3个元素，容量为5的意思是可以扩展到5个元素
	// fmt.Println(slice2)

	// // 使用切片
	// // 添加元素，切片容量可以根据需要自动扩展
	// // slice1 := make([]float32, 0) // 即使我给的是0，后面也可以append拓展
	// // slice1 = append(slice1, 1, 2, 3, 4) // [1, 2, 3, 4]
	// slice2 := make([]float32, 3, 5)
	// slice2 = append(slice2, 1, 2, 3, 4) // [0, 0, 0, 1, 2, 3, 4]
	// fmt.Println(len(slice2), cap(slice2)) // 7 12
	// fmt.Println(slice2)
	// // 长度变为7我可以理解，但是为什么容量变成12呢？
	// // 如果是两倍那应该是10，如果是原本的容量加四个元素那应该是9，为何是12？
	// // 解释：？？不知道


	// // 子切片 [start, end) 记住左闭右开 和python一样
	// sub1 := slice2[3:] // [1 2 3 4]
	// sub2 := slice2[:3] // [0 0 0]
	// sub3 := slice2[1:4] // [0 0 1]
	// // 合并切片
	// // 这里的...是解包操作符，用于将切片解包成一个个元素？？AI的解释
	// combined := append(sub1, sub2...) // [1, 2, 3, 4, 0, 0, 0]
	// fmt.Println(sub1, sub2, sub3)
	// fmt.Println(combined)
	

	// // 3.5 字典 和python的字典，java的hashmap差不多
	// // 仅声明
	// // 看下面赋值部分，方框里是键，后面是值
	// m1 := make(map[string]int)
	// // 声明时初始化
	// m2 := map[string]string{
	// 	"Sam": "Male",
	// 	"Alice": "Female",
	// }
	// // 赋值/修改
	// m1["Tom"] = 18

	// // 3.6 指针
	// // 指针即某个值的地址，类型定义时使用符号*，对一个已经存在的变量，使用 & 获取该变量的地址。
	// str := "Golang"
	// var p *string = &str // p 是指向 str 的指针
	// pp := &str
	// *p = "Hello" // 修改的是p所指向的地址的值，而不是修改p的值（p的值是地址）
	// fmt.Println(str) // Hello   同上，str 的值也发生了改变
	// fmt.Println(*pp) // Hello

	// fmt.Println(p) // str的地址,这三个都一样
	// fmt.Println(pp) 
	// fmt.Println(&str) 

	// // 传参问题
	// // 一般来说，指针通常在函数传递参数，或者给某个类型定义新的方法时使用。
	// // Go 语言中，参数是按值传递的，如果不使用指针，函数内部将会拷贝一份参数的副本，对参数的修改并不会影响到外部变量的值。
	// // 如果参数使用指针，对参数的传递将会影响到外部变量。

	// // 4.1 条件语句
	// age := 18
	// if age < 18 {
	// 	fmt.Printf("Kid")
	// } else {
	// 	fmt.Printf("Adult")
	// }

	// // 可以简写为：
	// if age := 18; age < 18 {
	// 	fmt.Printf("Kid")
	// } else {
	// 	fmt.Printf("Adult")
	// }

	// // 4.2 switch
	// // 在这里，使用了type 关键字定义了一个新的类型 Gender。
	// // 使用 const 定义了 MALE 和 FEMALE 2 个常量，Go 语言中没有枚举(enum)的概念，一般可以用常量的方式来模拟枚举。
	// // 24-3-9 没看懂
	// type Gender int8
	// const (
	// 	MALE   Gender = 1
	// 	FEMALE Gender = 2
	// )

	// gender := MALE
	// fmt.Println(reflect.TypeOf(gender).Kind()) // int8

	// switch gender {
	// case FEMALE:
	// 	fmt.Println("female")
	// case MALE:
	// 	fmt.Println("male")
	// default:
	// 	fmt.Println("unknown")
	// }
	// // male

	// // 和其他语言不同的地方在于，Go 语言的 switch 不需要 break，匹配到某个 case，执行完该 case 定义的行为后，默认不会继续往下执行。
	// // 如果需要继续往下执行，需要使用 fallthrough，例如：
	// switch gender {
	// case FEMALE:
	// 	fmt.Println("female")
	// 	fallthrough
	// case MALE:
	// 	fmt.Println("male")
	// 	fallthrough
	// default:
	// 	fmt.Println("unknown")
	// }
	// // 输出结果
	// // male
	// // unknown

	// // 4.3 for循环
	// // break和continue与其他语言一样
	// sum := 0
	// for i := 0; i < 10; i++ {
	// 	if sum > 50 {
	// 		break
	// 	}
	// 	sum += i
	// }
	// fmt.Println(sum) // 45

	// 对数组(arr)、切片(slice)、字典(map) 使用 for range 遍历：
	nums := []int{10, 20, 30, 40}
	for i, num := range nums {
		fmt.Println(i, num)
	}
	// 0 10
	// 1 20
	// 2 30
	// 3 40
	m2 := map[string]string{
		"Sam":   "Male",
		"Alice": "Female",
	}

	for key, value := range m2 {
		fmt.Println(key, value)
	}
	// Sam Male
	// Alice Female
	
}
