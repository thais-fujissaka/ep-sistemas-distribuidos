import grpc
from concurrent import futures
import time
import grpctests_pb2_grpc as pb2_grpc
import grpctests_pb2 as pb2
from google.protobuf.empty_pb2 import Empty

class TestService(pb2_grpc.TestsRPCServicer):
    def __init__(self, *args, **kwargs):
        pass

    #Método de retorno que retorna string
    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result}
        return pb2.MessageResponse(**result)
    
    #Método que retorna void
    def GetsVoid(self,request,context):
        return Empty()

    #Método que retorna valor longo
    def GetsLong(self, request, context):
        number1 = request.number
        result = number1
        response = pb2.Long_Response(result=result)
        return response

    #Método que retorna valor longo mas recebe 8 valores longos
    def GetsEightLongs(self, request, context):
        values = request.long_values
        result = sum(values)
        return pb2.Long_Response(result = result)

    #Método que retorna valor complexo (Classe)
    def ProcessClass(self, request, context):
        instance = request.instance
        result = instance.value
        return pb2.ProcessClassResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TestsRPCServicer_to_server(TestService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
