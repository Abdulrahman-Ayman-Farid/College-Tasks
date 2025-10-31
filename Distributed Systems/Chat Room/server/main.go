package main

import (
	"fmt"
	"log"
	"net"
	"net/http"
	"net/rpc"
	"sync"
)

// Message defines the structure for a single chat message.
type Message struct {
	User    string
	Content string
}

// HistoryReply is the structure for the reply from the server, containing all messages.
type HistoryReply struct {
	Messages []Message
}

// ChatRoom is the type that we'll register with the RPC server.
// It holds the chat history and a mutex to prevent race conditions.
type ChatRoom struct {
	history []Message
	mutex   sync.Mutex
}

// SendMessage is an RPC method for clients to send a message.
// It adds the message to the history and returns the updated history.
func (cr *ChatRoom) SendMessage(msg Message, reply *HistoryReply) error {
	cr.mutex.Lock()
	defer cr.mutex.Unlock()

	// Add the new message to our history
	cr.history = append(cr.history, msg)
	fmt.Printf("Received message from %s: %s\n", msg.User, msg.Content)

	// Return the full chat history to the client
	reply.Messages = cr.history
	return nil
}

// GetHistory is an RPC method for clients to fetch the entire chat history.
func (cr *ChatRoom) GetHistory(args struct{}, reply *HistoryReply) error {
	cr.mutex.Lock()
	defer cr.mutex.Unlock()

	// Return the full chat history
	reply.Messages = cr.history
	return nil
}

func main() {
	// Create a new ChatRoom instance
	chatRoom := new(ChatRoom)

	// Register the ChatRoom object with the RPC system.
	// This makes its methods available for remote calls.
	err := rpc.Register(chatRoom)
	if err != nil {
		log.Fatalf("Failed to register RPC object: %v", err)
	}

	// Use the default HTTP handler for RPC
	rpc.HandleHTTP()

	// Start an HTTP server on a specific port
	port := ":1234"
	listener, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("Failed to listen on port %s: %v", port, err)
	}

	fmt.Printf("✅ Chat server is running on port %s\n", port)
	fmt.Println("Waiting for clients to connect...")

	// Serve requests
	err = http.Serve(listener, nil)
	if err != nil {
		log.Fatalf("HTTP server error: %v", err)
	}
}