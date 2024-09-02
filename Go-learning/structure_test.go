package main

import (
	"fmt"
	"strings" // Import the "strings" package
	"testing"
)

func BenchmarkStructure(b *testing.B) {
	A := []string{"Hello", "World"}
	result := strings.Join(A, " ") // Use the correct method name "Join" instead of "join"
	fmt.Println(result)
}
