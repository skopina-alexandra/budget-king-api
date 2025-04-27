package main

import (
	config_pkg "budget-king/internal/config"
	"fmt"
)

func main() {
	config := config_pkg.MustLoad()
	fmt.Println(config)
}
