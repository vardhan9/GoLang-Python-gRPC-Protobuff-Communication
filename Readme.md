AIM: To establish communication between python server and Go client with protocol buffer

Steps to follow 

1. Create .proto file depending upon your requirements
2. Run the following command to generate Go files : protoc --go_out=. --go-grpc_out=. communication.proto
3. Files with names communication_grpc.pb.go and communication_pb.go will created inside the protoc folder
4. Run the following command to generate Python files: python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. communication.proto
5. Files with name communication_pb2_grpc.py and communication_pb2.py will be create in the same location as communication.proto

6. Initate the modules with command: go mod init golang-py-communication (your module name)
7. This will create go.mod file
9. Run the command : go mod tidy, To add module requirements and sums
10. Now create folders Client and Server

11. In Server folder, create server.py file and add code.
12. Move communication_pb2_grpc.py and communication_pb2.py files to the server folder.
13. From terminal, cd GoLang-Python-gRPC-Protobuff-Communication\Server and run python server with command: python server.py
14. This will starts the server in the given port, 50051 in this case and you can "Server Started".

15. In Client folder, create client.go file and add code.
16. From GoLang-Python-gRPC-Protobuff-Communication, give comman: go run ./Client
17. This should return "Response from server: Received: Hello from Go Client"
18. Communication is established between Python server and Go client with Protocol buffers.