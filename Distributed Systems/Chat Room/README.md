# 💬 Simple Chatroom in Go

A lightweight, terminal-based real-time chatroom application built with Go's `net/rpc` package. This project demonstrates client-server architecture and remote procedure calls.

## 🎥 Demo

**[📹 Watch Running Demo](https://drive.google.com/open?id=1ncO8oV-Yt-2En0u-2n2rP9guNpXw2bXq&usp=drive_fs)**

## ✨ Features

- **Multi-Client Support**: Multiple users can chat simultaneously
- **Real-time Updates**: Instant message delivery across all clients
- **Thread-Safe**: Uses mutex locks to prevent race conditions
- **Chat History**: Server maintains conversation history during runtime

## 🚀 Quick Start

### Prerequisites
- Go 1.25 or higher ([Download](https://go.dev/dl/))

### Running the Application

**1. Start the Server** (in terminal 1):
```bash
go run server/main.go
```

**2. Start Client(s)** (in terminal 2, 3, etc.):
```bash
go run client/main.go
```

**3. Chat!**
- Enter your username when prompted
- Type messages and press Enter
- Type `exit` to disconnect

##  Project Structure

```
chat-room/
├── server/main.go    # RPC server (port 1234)
└── client/main.go    # Terminal client
```

## 🔧 How It Works

**Server:**
- Listens on port `1234` using Go's `net/rpc` over HTTP
- Stores chat history in memory with thread-safe mutex locks
- Provides two RPC methods: `SendMessage` and `GetHistory`

**Client:**
- Connects to server via RPC
- Sends messages and receives updated chat history
- Auto-clears terminal for clean UI

## 📝 License

MIT License - Created as a college assignment for Distributed Systems course.