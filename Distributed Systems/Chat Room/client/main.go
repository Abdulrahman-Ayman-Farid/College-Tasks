package main

import (
	"bufio"
	"fmt"
	"log"
	"net/rpc"
	"os"
	"strings"
)

// Message defines the structure for a single chat message.
// This must match the server's definition.
type Message struct {
	User    string
	Content string
}

// HistoryReply is the structure for the reply from the server.
// This must also match the server's definition.
type HistoryReply struct {
	Messages []Message
}

// printHistory clears the screen (in a simple way) and prints all messages.
func printHistory(messages []Message) {
	// A simple way to "clear" the terminal for a cleaner look
	fmt.Print("\033[H\033[2J")
	fmt.Println("--- Chat History ---")
	if len(messages) == 0 {
		fmt.Println("No messages yet. Be the first to say something!")
	} else {
		for _, msg := range messages {
			fmt.Printf("[%s]: %s\n", msg.User, msg.Content)
		}
	}
	fmt.Println("--------------------")
	fmt.Print("Enter message ('exit' to quit): ")
}

func main() {
	// Connect to the RPC server
	client, err := rpc.DialHTTP("tcp", "localhost:1234")
	if err != nil {
		// Handle the error if the server is down
		log.Fatalf("❌ Server is not running. Please start the server and try again. Error: %v", err)
	}
	defer client.Close()

	fmt.Println("✅ Connected to the chat server.")

	// Get username from the user
	fmt.Print("Please enter your name: ")
	reader := bufio.NewReader(os.Stdin)
	username, _ := reader.ReadString('\n')
	username = strings.TrimSpace(username)

	// --- Initial fetch of chat history ---
	var initialReply HistoryReply
	err = client.Call("ChatRoom.GetHistory", struct{}{}, &initialReply)
	if err != nil {
		log.Printf("Error fetching initial history: %v\n", err)
	}
	printHistory(initialReply.Messages)

	// --- Main loop to send messages ---
	for {
		// Read a full line of input from the user
		userInput, _ := reader.ReadString('\n')
		userInput = strings.TrimSpace(userInput)

		// Check if the user wants to exit
		if userInput == "exit" {
			fmt.Println("Disconnecting from chat. Goodbye!")
			break
		}

		if userInput == "" {
			continue // Don't send empty messages
		}

		// Prepare the message and the reply container
		args := Message{User: username, Content: userInput}
		var reply HistoryReply

		// Call the remote procedure "SendMessage" on the server
		err = client.Call("ChatRoom.SendMessage", args, &reply)
		if err != nil {
			// Handle cases where the server might go down during the session
			log.Fatalf("Error calling remote procedure: %v. Server may have disconnected.", err)
		}

		// Print the updated history received from the server
		printHistory(reply.Messages)
	}
}