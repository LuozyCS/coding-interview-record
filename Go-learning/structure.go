package main

import (
	"fmt"
)

func main() {
	// var ss string
	// ss = "Hello"
	// fmt.Println(&ss)
	// for _, v := range ss {
	// 	fmt.Println("\n", v)
	// }
	// ss = "no Hello"
	// ss[0] = 'Y' // string不能修改，只能重新赋值
	// strByte := []byte(ss)
	// fmt.Println(strByte)

	// s1 := "Hello"
	// s2 := "World"
	// builder := strings.Builder{}
	// builder.WriteString(s1)
	// builder.WriteString(s2)
	// result := builder.String()
	// fmt.Println(result)

	////////////////////////////////////////
	// s := []int{0, 1, 2, 3, 4}
	// fmt.Println(s)

	// s1 := append(s[:1], s[2:]...)
	// fmt.Println("s1 cap:", cap(s1))
	// fmt.Println("s1 len:", len(s1))
	// fmt.Println(s1)
	// fmt.Println(s)
	////////////////////////////////////////

	m := make(map[int]int)
	m[0] = 1
	m[1] = 2
	if n, has := m[1]; true {
		fmt.Println(n, has)
	}
}
