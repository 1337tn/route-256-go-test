package main

import (
	"bufio"
	"fmt"
	"os"
)

var factVal uint64 = 1
var n, t int

func factorial(n int) uint64 {
	if n < 0 {
		fmt.Print("Factorial of negative number doesn't exist.")
	} else {
		for i := 1; i <= n; i++ {
			factVal *= uint64(i) // mismatched types int64 and int
		}

	}
	return factVal
}

func main() {
	//TODO: finish
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	parsed, _ := fmt.Sscanf(text, "%d %d", &n, &t)
	fmt.Println(parsed, n, t)
}
