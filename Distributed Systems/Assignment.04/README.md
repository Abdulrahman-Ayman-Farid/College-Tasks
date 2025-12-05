# Assignment 04: Real-Time Chat System with Broadcasting

## Description
This assignment modifies the previous RPC-based chat system to use real-time broadcasting with Go concurrency. The system supports multiple clients connecting to a single server, with messages broadcasted in real-time to all connected clients.

## Features
- **Real-Time Broadcasting**: Messages are broadcasted instantly to all connected clients using goroutines and channels.
- **Client Join Notifications**: When a client joins, all other clients are notified with "User [ID] joined".
- **No Self-Echo**: Clients do not receive their own messages or join notifications.
- **Message History**: New clients receive the full chat history upon joining.
- **Concurrency**: Uses goroutines for handling multiple clients concurrently and channels for message broadcasting.
- **Synchronization**: Shared client list is protected with a Mutex for thread safety.

## How to Run

### Server
1. Navigate to the server directory:
   ```
   cd "Distributed Systems/Assignment.04/Chat Room/server"
   ```
2. Run the server:
   ```
   go run main.go
   ```
   The server will start on port 1234.

### Client
1. Open a new terminal and navigate to the client directory:
   ```
   cd "Distributed Systems/Assignment.04/Chat Room/client"
   ```
2. Run the client:
   ```
   go run main.go
   ```
3. Type messages and press Enter to send. Type 'exit' to quit.

### Multiple Clients
Open multiple terminals and run the client in each to simulate multiple users chatting.

## Implementation Details
- **Server**: Manages client connections, broadcasts messages, and maintains chat history.
- **Client**: Connects to the server, sends user input as messages, and displays received messages.
- **Message Types**: 
  - `join`: Notifies when a user joins.
  - `message`: Regular chat messages.
  - `history`: Sent to new clients with previous messages.
- **Concurrency**: Each client has dedicated goroutines for reading and writing, with a central broadcast goroutine.

## Requirements
- Go 1.16 or later
- Standard library only (no external dependencies)