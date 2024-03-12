package main

import (
	"example/calc"
	"fmt"

	"rsc.io/quote"
)

// 运行 go run .
// 将会自动触发第三方包 rsc.io/quote的下载.
// (我自己尝试的时候并没有自动下载，而是手动运行go get rsc.io/quote)
// 具体的版本信息也记录在了go.mod中.
func main() {
	fmt.Println(quote.Hello()) // Ahoy, world!

	// 在 package main 中如何使用 package cal 中的 Add 函数呢？
	// import 模块名/子目录名 即可，修改后的 main 函数如下：

	fmt.Println(calc.Add(10, 3))
}
