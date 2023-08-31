import grpc
from concurrent import futures
import communication_pb2
import communication_pb2_grpc

class CommunicationServicer(communication_pb2_grpc.CommunicationServicer):
    def SendRequest(self, request, context):
        response = communication_pb2.Response(reply=f"Received: {request.message}")
        print("recived message from client")
        return response

def run_server():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServicer_to_server(CommunicationServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")
    server.wait_for_termination()
    

if __name__ == "__main__":
    run_server()