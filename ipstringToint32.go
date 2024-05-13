package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	ip := "192.168.1.1"
	res := ip2int32(ip)
	fmt.Println(res)
}

func ip2int32(ip string) int {
	parts := strings.Split(ip, ".")
	// fmt.Print(parts)
	var res uint32
	for _, part := range parts {
		num, _ := strconv.Atoi(part)

		res = (res << 8) + uint32(num)
	}
	return int(res)
}
