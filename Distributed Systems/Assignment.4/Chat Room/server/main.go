package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"sync"
)

// Message represents a chat message or event
type Message struct {
	Type    string `json:"type"` // "join", "message", "history"
	User    string `json:"user"`
	Content string `json:"content"`
}

// Client represents a connected client
type Client struct {
	id   string
	conn net.Conn
	send chan Message
}

// Server manages the chat room
type Server struct {
	clients   map[string]*Client
	history   []Message
	mutex     sync.Mutex
	broadcast chan Message
}

// run handles broadcasting messages to clients
func (s *Server) run() {
	for msg := range s.broadcast {
		s.mutex.Lock()
		for id, client := range s.clients {
			// No self-echo for messages and joins
			if (msg.Type == "message" && id == msg.User) || (msg.Type == "join" && id == msg.User) {
				continue
			}
			select {
			case client.send <- msg:
			default:
				// Client disconnected
				close(client.send)
				delete(s.clients, id)
			}
		}
		s.mutex.Unlock()
	}
}

// handleConnection handles a new client connection
func (s *Server) handleConnection(conn net.Conn) {
	s.mutex.Lock()
	id := fmt.Sprintf("User%d", len(s.clients)+1)
	client := &Client{
		id:   id,
		conn: conn,
		send: make(chan Message, 256),
	}
	s.clients[id] = client
	s.mutex.Unlock()

	// Send history to new client
	for _, histMsg := range s.history {
		historyMsg := Message{Type: "history", User: histMsg.User, Content: histMsg.Content}
		client.send <- historyMsg
	}

	// Broadcast join message
	joinMsg := Message{Type: "join", User: id, Content: "joined"}
	s.broadcast <- joinMsg

	// Start goroutines for this client
	go client.writePump()
	go s.readPump(client)
}

// writePump sends messages to the client
func (c *Client) writePump() {
	for msg := range c.send {
		data, err := json.Marshal(msg)
		if err != nil {
			log.Printf("Error marshaling message: %v", err)
			continue
		}
		fmt.Fprintf(c.conn, "%s\n", data)
	}
	c.conn.Close()
}

// readPump reads messages from the client
func (s *Server) readPump(client *Client) {
	scanner := bufio.NewScanner(client.conn)
	for scanner.Scan() {
		var msg Message
		err := json.Unmarshal(scanner.Bytes(), &msg)
		if err != nil {
			log.Printf("Error unmarshaling message: %v", err)
			continue
		}
		msg.User = client.id
		msg.Type = "message" // Ensure it's a message

		// Add to history
		s.mutex.Lock()
		s.history = append(s.history, msg)
		s.mutex.Unlock()

		// Broadcast the message
		s.broadcast <- msg
	}

	// Client disconnected
	s.mutex.Lock()
	delete(s.clients, client.id)
	s.mutex.Unlock()
	close(client.send)
}

func main() {
	server := &Server{
		clients:   make(map[string]*Client),
		history:   []Message{},
		broadcast: make(chan Message),
	}

	go server.run()

	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}
	defer listener.Close()

	fmt.Println("Chat server started on :1234")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("Failed to accept connection: %v", err)
			continue
		}
		go server.handleConnection(conn)
	}
}
