package main

import (
	"fmt"
	"time"
)

// var wg sync.WaitGroup

// func download_sync(url string) {
// 	fmt.Println("start to download", url)
// 	time.Sleep(time.Second) // 模拟下载耗时
// 	wg.Done()               // ?
// }

// func download(url string) {
// 	fmt.Println("start to download", url)
// 	time.Sleep(time.Second) // 模拟下载耗时
// }

var ch = make(chan string, 10) // 创建大小为 10 的缓冲信道

func download_channel(url string) {
	fmt.Println("start to download", url)
	time.Sleep(time.Second)
	ch <- url // 将 url 发送给信道
	// time.Sleep(time.Second) // 即使在这里加一行，等待从信道 ch 中接收消息的循环结束的时间也是1s。
}

func main() {
	fmt.Println("Hello World!")

	// // sec7 并发编程(goroutine)
	// // Go 语言提供了 sync 和 channel 两种方式支持协程(goroutine)的并发。
	// // 协程的概念：https://zhuanlan.zhihu.com/p/172471249
	// // 协程并不增加线程的数量。
	// // 只是在线程的基础之上通过分时复用的方式运行多个协程，而且协程的切换在用户态完成，切换的代价比线程从用户态到内核态的代价小很多。

	// // 7.1 sync
	// // 例如我们希望并发下载 N 个资源，多个并发协程之间不需要通信，
	// // 那么就可以使用 sync.WaitGroup，等待所有并发协程执行结束。
	// t1 := time.Now()
	// for i := 0; i < 3; i++ {
	// 	wg.Add(1)                                  // 为 wg 添加一个计数，wg.Done()，减去一个计数。
	// 	go download_sync("a.com/" + string(i+'0')) // 启动新的协程并发执行 download 函数。
	// 	// (和Ascii码那个道理一样）在 Go 语言中，string(i) 将整数 i 转换为其对应的 Unicode 字符。例如，如果 i 是 65，string(i) 将返回 "A"，因为 65 是 "A" 的 Unicode 码。
	// 	// 当你写 string(i+'0')，你实际上是在将 i 的值加上 '0' 的 Unicode 码（48），然后将结果转换为对应的字符。例如，如果 i 是 1，i+'0' 就是 49，string(i+'0') 就会返回 "1"。
	// }
	// wg.Wait() // 等待所有并发协程执行结束。
	// fmt.Println("Done")

	// t2 := time.Now()
	// fmt.Println("sync time:", t2.Sub(t1)) // sync time: 1.001156875s
	// // 对比协程和直接运行的时间
	// for i := 0; i < 3; i++ {
	// 	download("a.com/" + string(i+'0'))
	// }
	// fmt.Println("normal time:", time.Since(t2)) // normal time: 3.002592208s

	// 7.2 channel
	// 使用 channel 信道，可以在协程之间传递消息。阻塞等待并发协程返回消息。
	t10 := time.Now()
	for i := 0; i < 3; i++ {
		go download_channel("a.com/" + string(i+'0'))
	}
	t20 := time.Now()
	fmt.Println(t20.Sub(t10))
	for i := 0; i < 3; i++ {
		msg := <-ch // 等待从信道 ch 中接收消息
		fmt.Println("finish", msg)
	}
	fmt.Println(time.Since(t20)) // 1s
	fmt.Println("Done")
}
