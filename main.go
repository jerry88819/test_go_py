package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os/exec"
)

type Person struct {
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Email string `json:"email"`
}


func main() {
	pythonScript := "hello.py"
	pythonArgs := []string{"John Doe", "400", "johndoe@example.com"}

	// 创建一个 cmd 对象来运行 Python 脚本
	cmd := exec.Command("python", append([]string{pythonScript}, pythonArgs...)...)

	// 设置标准输出
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		fmt.Println("Error creating stdout pipe:", err)
		return
	}
	defer stdout.Close()

	// 启动 Python 解释器
	err = cmd.Start()
	if err != nil {
		fmt.Println("Error starting Python script:", err)
		return
	}

	// 读取 Python 脚本的输出
	outputData, err := ioutil.ReadAll(stdout)
	if err != nil {
		fmt.Println("Error reading data from Python script:", err)
		return
	}

	// 等待 Python 脚本执行完成
	err = cmd.Wait()
	if err != nil {
		fmt.Println("Error waiting for Python script:", err)
		return
	}

	// 解析 JSON 数据到 Golang 的结构体
	var person Person
	err = json.Unmarshal(outputData, &person)
	if err != nil {
		fmt.Println("Error unmarshaling JSON data:", err)
		return
	}

	// 输出 Golang 中的数据
	fmt.Println("Name:", person.Name)
	fmt.Println("Age:", person.Age)
	fmt.Println("Email:", person.Email)


	// fmt.Println("hello")
	
	
	// cmd := exec.Command("python","hello.py")
    // cmd.Stdout = os.Stdout
    // cmd.Stderr = os.Stderr
    
	
	// err := cmd.Run()
	// if err != nil {
	// 	fmt.Println("err")
	// } // if()
} // main()