// calc_test.go
package main

import "testing"

func TestAdd(t *testing.T) {
	if ans := add(1, 2); ans != 3 {
		t.Error("add(1, 2) should be equal to 3")
	}
}

// 成功的输出 go test -v
// === RUN   TestAdd
// --- PASS: TestAdd (0.00s)
// PASS
// ok      calc.go 0.260s
