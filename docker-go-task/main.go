package main
import ("fmt"; "net/http"; "time")

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Task Complete! Time: %s", time.Now().Format(time.RFC1123))
	})
	fmt.Println("Server on :8080")
	http.ListenAndServe(":8080", nil)
}