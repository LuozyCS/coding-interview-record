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

	// 数组操作比较麻烦，数组长度无法改变，所以一般用切片




}
