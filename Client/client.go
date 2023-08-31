package main

import (
	"context"
	"fmt"
	"log"

	communication"golang-py-communication/protoc"
	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Could not connect: %v", err)
	}
	defer conn.Close()

	client := communication.NewCommunicationClient(conn)

	request := &communication.Request{Message: "Hello from Go Client"}
	response, err := client.SendRequest(context.Background(), request)
	if err != nil {
		log.Fatalf("Error sending request: %v", err)
	}

	fmt.Printf("Response from server: %s\n", response.GetReply())
}
