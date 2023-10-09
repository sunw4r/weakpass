package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
	"time"
)

func main() {
	// banner
	fmt.Fprintln(os.Stderr, `
          _______  _______  _        _______  _______  _______  _______         _ 
|\     /|(  ____ \(  ___  )| \    /\(  ____ )(  ___  )(  ____ \(  ____ \       / )
| )   ( || (    \/| (   ) ||  \  / /| (    )|| (   ) || (    \/| (    \/   _  / / 
| | _ | || (__    | (___) ||  (_/ / | (____)|| (___) || (_____ | (_____   (_)( (  
| |( )| ||  __)   |  ___  ||   _ (  |  _____)|  ___  |(_____  )(_____  )     | |  
| || || || (      | (   ) ||  ( \ \ | (      | (   ) |      ) |      ) |   _ ( (  
| () () || (____/\| )   ( ||  /  \ \| )      | )   ( |/\____) |/\____) |  (_) \ \ 
(_______)(_______/|/     \||_/    \/|/       |/     \|\_______)\_______)       \_)

                                by: @sunw4r
                                                                                  
`)

	// Command line arguments
	bigFlag := flag.Bool("b", false, "Generate more permutations of passwords (recommended for offline brute)")
	webFlag := flag.Bool("w", true, "Generate a smaller amount of permutations (recommended for online spray)")
	companyFlag := flag.String("c", "", "Company Name (one word) to be used in permutations")
	outputFlag := flag.String("o", "", "File to store the passwords. If not specified, it will be printed to stdout")
	flag.Parse()

	if *companyFlag == "" || (!*bigFlag && !*webFlag) {
		flag.Usage()
		os.Exit(1)
	}

	company := strings.ToLower(*companyFlag)
	companyCap := strings.Title(company)
	companyFullCap := strings.ToUpper(company)

	caseTypes := []string{companyCap, company, companyFullCap}
	webCaseTypes := []string{companyCap, company}

	currentYear := time.Now().Year()
	currentYearM := currentYear - 1
	currentYearMM := currentYear - 2
	currentYearMMM := currentYear - 3
	currentYearMMMM := currentYear - 4
	currentYearMMMMM := currentYear - 5
	currentYearP := currentYear + 1

	numbers := []string{
		fmt.Sprintf("%d", currentYear),
		fmt.Sprintf("%d", currentYearM),
		fmt.Sprintf("%d", currentYearMM),
		fmt.Sprintf("%d", currentYearMMM),
		fmt.Sprintf("%d", currentYearMMMM),
		fmt.Sprintf("%d", currentYearMMMMM),
		fmt.Sprintf("%d", currentYearP),
		"1",
		"12",
		"123",
		"1234",
		"12345",
	}

	webNumbers := []string{
		fmt.Sprintf("%d", currentYear),
		fmt.Sprintf("%d", currentYearM),
		"123",
	}

	specials := []string{"@", "", "!", "*", "#"}

	webSpecials := []string{"@", ""}

	var wpwdlist []string

	if *bigFlag {
		for _, x := range caseTypes {
			for _, y := range numbers {
				for _, z := range specials {
					wpwdlist = append(wpwdlist, x+z+y, x+y+z, y+x+z, y+z+x, z+y+x, z+x+y)
				}
			}
		}
	} else if *webFlag {
		for _, x := range webCaseTypes {
			for _, y := range webNumbers {
				for _, z := range webSpecials {
					wpwdlist = append(wpwdlist, x+z+y)
				}
			}
		}
	}

	// Remove duplicates
	outputMap := make(map[string]struct{})
	for _, password := range wpwdlist {
		outputMap[password] = struct{}{}
	}
	var output []string
	for password := range outputMap {
		output = append(output, password)
	}

	// Print or save to file
	if *outputFlag != "" {
		file, err := os.Create(*outputFlag)
		if err != nil {
			fmt.Fprintln(os.Stderr, "Error opening output file:", err)
			os.Exit(1)
		}
		defer file.Close()

		for _, password := range output {
			fmt.Fprintln(file, password)
		}
	} else {
		for _, password := range output {
			fmt.Println(password)
		}
	}
}
