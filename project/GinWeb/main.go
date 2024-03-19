package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	//  根据不同的HTTP请求会调用不同的处理函数
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/hello", helloHandler)
	log.Fatal((http.ListenAndServe(":9999", nil))) // 启动Web服务
	// 而第二个参数则代表处理所有的HTTP请求的实例，nil 代表使用标准库中的实例处理。
	// 第二个参数，则是我们基于net/http标准库实现Web框架的入口。
}

// handler echoes r.URL.Path
func indexHandler(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "URL.Path = %q\n", req.URL.Path)
}

// handler echoes r.URL.Header
func helloHandler(w http.ResponseWriter, req *http.Request) {
	for k, v := range req.Header {
		fmt.Fprintf(w, "Header[%q] = %q\n", k, v)
	}
}
