package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"os"
	"strings"
)

// Message represents a chat message or event
type Message struct {
	Type    string `json:"type"`
	User    string `json:"user"`
	Content string `json:"content"`
}

// readPump reads messages from the server and prints them
func readPump(conn net.Conn) {
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		var msg Message
		err := json.Unmarshal(scanner.Bytes(), &msg)
		if err != nil {
			log.Printf("Error unmarshaling message: %v", err)
			continue
		}
		if msg.Type == "history" || msg.Type == "message" || msg.Type == "join" {
			fmt.Printf("[%s]: %s\n", msg.User, msg.Content)
		}
	}
}

func main() {
	conn, err := net.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatalf("Failed to connect to server: %v", err)
	}
	defer conn.Close()

	fmt.Println("Connected to chat server. Type 'exit' to quit.")

	// Start reading messages from server
	go readPump(conn)

	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print("Enter message: ")
		line, err := reader.ReadString('\n')
		if err != nil {
			log.Printf("Error reading input: %v", err)
			break
		}
		line = strings.TrimSpace(line)
		if line == "exit" {
			break
		}
		if line == "" {
			continue
		}

		msg := Message{Type: "message", Content: line}
		data, err := json.Marshal(msg)
		if err != nil {
			log.Printf("Error marshaling message: %v", err)
			continue
		}
		fmt.Fprintf(conn, "%s\n", data)
	}

	fmt.Println("Disconnected from chat.")
}