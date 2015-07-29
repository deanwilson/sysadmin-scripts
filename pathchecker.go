package main

import (
	"fmt"
	"os"
	"regexp"
	"sort"
	"strings"
)

func main() {
	env_path := os.Getenv("PATH")
	paths := strings.Split(env_path, ":")

	sort.Strings(paths)

	for _, path := range paths {
		var errors []string

		stat, err := os.Stat(path)
		if err != nil {
			fmt.Println(path)
			fmt.Println(" - " + err.Error())
			continue
		}

		if !stat.IsDir() {
			errors = append(errors, "not a directory")
		}

		mode := stat.Mode().String()
		if matched, _ := regexp.MatchString("d....w", mode); matched {
			errors = append(errors, "group writable permissions are too open - "+mode)
		}

		if matched, _ := regexp.MatchString("d.......w.", mode); matched {
			errors = append(errors, "other writable permissions are too open - "+mode)
		}

		if len(errors) > 0 {
			fmt.Println(path)
			for _, err := range errors {
				fmt.Println(" - " + err)
			}
		}
	}
}
