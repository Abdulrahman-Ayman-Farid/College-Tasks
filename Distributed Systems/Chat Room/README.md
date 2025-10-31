# 💬 Simple Chatroom in Go

[![Go Version](https://img.shields.io/badge/Go-1.18%2B-00ADD8?style=flat&logo=go)](https://go.dev/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A lightweight, terminal-based real-time chatroom application built with Go's native `net/rpc` package. This project demonstrates client-server architecture, concurrent programming, and remote procedure calls in Go.

![Chatroom Demo](https://via.placeholder.com/800x400/00ADD8/ffffff?text=Terminal+Based+Chatroom)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project is a simple, terminal-based chatroom application that allows multiple users to communicate in real-time through a central server. Built entirely in Go using the `net/rpc` package, it showcases fundamental concepts in distributed systems and network programming.

## ✨ Features

-   **🔄 Client-Server Architecture**: Built with Go's native RPC (Remote Procedure Call) library for efficient communication
-   **💾 Persistent Chat History**: Server maintains complete conversation history for the duration of its runtime
-   **⚡ Real-time Updates**: Instant message delivery and synchronized chat history across all clients
-   **👥 Multi-Client Support**: Multiple users can connect simultaneously from different terminals
-   **🛡️ Robust Error Handling**: Graceful handling of connection failures and server disconnections
-   **🔒 Thread-Safe Operations**: Uses mutex locks to prevent race conditions in concurrent access
-   **🎨 Clean Terminal UI**: Auto-clearing terminal display for a smooth chat experience

## 🏗️ Architecture

```
┌─────────────┐         RPC over HTTP          ┌─────────────┐
│             │◄──────────────────────────────►│             │
│  Client 1   │                                 │             │
│             │         TCP :1234               │             │
└─────────────┘                                 │             │
                                                │   Server    │
┌─────────────┐         RPC over HTTP          │             │
│             │◄──────────────────────────────►│  (Stores    │
│  Client 2   │                                 │   History)  │
│             │         TCP :1234               │             │
└─────────────┘                                 │             │
                                                │             │
┌─────────────┐         RPC over HTTP          │             │
│             │◄──────────────────────────────►│             │
│  Client N   │                                 │             │
│             │         TCP :1234               │             │
└─────────────┘                                 └─────────────┘
```

### Communication Flow

1. **Initial Connection**: Client connects to server via RPC and fetches existing chat history
2. **Sending Messages**: Client sends message to server using `SendMessage` RPC call
3. **History Update**: Server appends message and returns updated history to client
4. **Display**: Client clears screen and displays updated chat history

---

## 🚀 Getting Started

### Prerequisites

Before running this application, ensure you have:

-   **Go** (version 1.18 or higher) - [Download Here](https://go.dev/dl/)
-   **Terminal/Command Prompt** access
-   **Text Editor** (VS Code, Vim, etc.) for viewing/editing code

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/go-chatroom.git
    cd go-chatroom
    ```

2.  **Verify Go installation:**
    ```bash
    go version
    ```
    You should see output like: `go version go1.21.0 windows/amd64`

### Running the Application

#### Step 1: Start the Server

Open a terminal and start the server:

```bash
go run server/main.go
```

**Expected Output:**
```
✅ Chat server is running on port :1234
Waiting for clients to connect...
```

The server is now listening for client connections on port 1234.

#### Step 2: Start Client(s)

Open a **new terminal window** (keep the server running) and start a client:

```bash
go run client/main.go
```

**You'll be prompted to enter your username:**
```
✅ Connected to the chat server.
Please enter your name: Alice
```

#### Step 3: Start Additional Clients (Optional)

To simulate a multi-user chatroom:
- Open another terminal window
- Run `go run client/main.go` again
- Enter a different username

Each client will see the same shared chat history!

#### Step 4: Start Chatting

- Type your message and press **Enter** to send
- Type `exit` to disconnect from the chatroom
- Press **Ctrl+C** to force quit

---

## 📖 Usage

### Sending Messages

After connecting and entering your username, simply type your message:

```
Enter message ('exit' to quit): Hello everyone!
```

The chat history will update immediately showing your message.

### Viewing Chat History

All messages are displayed in chronological order:

```
--- Chat History ---
[Alice]: Hello everyone!
[Bob]: Hi Alice!
[Charlie]: Hey folks!
--------------------
Enter message ('exit' to quit): 
```

### Disconnecting

To leave the chatroom:
- Type `exit` and press Enter, OR
- Press `Ctrl+C` to force close

---

## 📁 Project Structure

```
chat-room/
│
├── README.md           # Project documentation
│
├── server/
│   └── main.go        # Server implementation
│                      # - Handles RPC requests
│                      # - Stores chat history
│                      # - Manages concurrent access
│
└── client/
    └── main.go        # Client implementation
                       # - Connects to server
                       # - Sends/receives messages
                       # - Displays chat UI
```

---

## 🔧 Technical Details

### Server Architecture (`server/main.go`)

The server acts as the central authority for the chatroom, managing all message storage and distribution.

#### Key Components:

**1. Data Structures**
```go
type Message struct {
    User    string  // Username of the sender
    Content string  // Message content
}

type ChatRoom struct {
    history []Message  // Stores all messages
    mutex   sync.Mutex // Prevents race conditions
}
```

**2. Thread Safety**
- Uses `sync.Mutex` to lock the `history` slice during read/write operations
- Prevents race conditions when multiple clients access the server simultaneously
- Ensures data consistency across concurrent requests

**3. RPC Methods**

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `SendMessage` | `Message` | `HistoryReply` | Appends new message and returns full history |
| `GetHistory` | `struct{}` | `HistoryReply` | Fetches current chat history |

**4. Network Configuration**
- **Protocol**: HTTP over TCP
- **Port**: 1234
- **RPC Transport**: Uses Go's built-in `net/rpc` over HTTP
- **Listener**: TCP listener on `localhost:1234`

#### Server Workflow:

```
1. Initialize ChatRoom with empty history
2. Register ChatRoom with RPC system
3. Setup HTTP handler for RPC
4. Start TCP listener on port 1234
5. Accept and handle client connections
   ├─► SendMessage: Add to history & return updated history
   └─► GetHistory: Return current history
```

---

### Client Architecture (`client/main.go`)

The client provides a user-friendly terminal interface for interacting with the chatroom.

#### Key Components:

**1. Connection Management**
```go
client, err := rpc.DialHTTP("tcp", "localhost:1234")
```
- Establishes HTTP-based RPC connection to server
- Includes robust error handling for connection failures
- Gracefully exits if server is unavailable

**2. User Input Handling**
- Uses `bufio.NewReader` for reading full lines (handles spaces)
- Trims whitespace from input
- Validates non-empty messages before sending

**3. Main Event Loop**
```
1. Prompt for username
2. Fetch initial chat history (GetHistory RPC)
3. Display history
4. Enter message loop:
   ├─► Read user input
   ├─► Check for 'exit' command
   ├─► Send message via SendMessage RPC
   ├─► Receive updated history
   └─► Clear screen and display updated history
```

**4. UI Features**
- `printHistory()` function clears terminal for clean display
- Shows all messages in `[Username]: Message` format
- Displays prompt for next message
- Handles empty chat history gracefully

#### Error Handling:

- **Connection Failure**: Exits with friendly error message
- **Empty Messages**: Ignored (not sent to server)
- **Server Disconnection**: Fatal error with informative message
- **User Exit**: Clean disconnection with goodbye message

---

### RPC Communication Protocol

#### Message Sending Flow:
```
Client                          Server
  │                               │
  ├─── SendMessage(msg) ────────►│
  │                               ├─ Lock mutex
  │                               ├─ Append to history
  │                               ├─ Unlock mutex
  │◄── HistoryReply(messages) ───┤
  │                               │
  └─ Display updated history      │
```

#### History Fetching Flow:
```
Client                          Server
  │                               │
  ├─── GetHistory() ─────────────►│
  │                               ├─ Lock mutex
  │                               ├─ Read history
  │                               ├─ Unlock mutex
  │◄── HistoryReply(messages) ───┤
  │                               │
  └─ Display history              │
```

---

## 🎓 Learning Outcomes

This project demonstrates:

- ✅ **Remote Procedure Calls (RPC)** in Go
- ✅ **Concurrent Programming** with goroutines and mutexes
- ✅ **Client-Server Architecture** design patterns
- ✅ **Network Programming** with TCP/HTTP
- ✅ **Error Handling** and graceful degradation
- ✅ **User Input Processing** and validation
- ✅ **Terminal UI** development

---

## 🐛 Troubleshooting

### Server won't start
- **Check port availability**: Ensure port 1234 is not in use
- **Firewall**: Make sure your firewall allows connections on port 1234

### Client can't connect
- **Server running?**: Verify the server is started first
- **Correct address?**: Confirm connecting to `localhost:1234`
- **Go installed?**: Run `go version` to verify installation

### Messages not appearing
- **Multiple terminals**: Ensure server and clients are in separate terminals
- **Network issues**: Check for any network connectivity problems

---

## 🚀 Future Enhancements

Potential improvements for this project:

- [ ] Add persistent storage (database/file system)
- [ ] Implement user authentication
- [ ] Add private messaging between users
- [ ] Create a web-based UI
- [ ] Add message timestamps
- [ ] Implement chat rooms/channels
- [ ] Add typing indicators
- [ ] Support message editing/deletion
- [ ] Add file sharing capabilities
- [ ] Implement end-to-end encryption

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Created as part of a college assignment to demonstrate distributed systems concepts in Go.

---

## 🙏 Acknowledgments

- Go's `net/rpc` package documentation
- Go community for excellent learning resources
- College assignment guidelines and requirements

---

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**⭐ If you found this project helpful, please consider giving it a star!**