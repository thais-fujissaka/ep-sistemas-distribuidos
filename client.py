import grpc
import grpctests_pb2_grpc as pb2_grpc
import grpctests_pb2 as pb2
import time
from google.protobuf.empty_pb2 import Empty

class TesterClient(object):
    def __init__(self):
        self.host = '192.168.0.101'
        self.server_port = 50051

        # Inicia o canal
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
        
        # Liga o cliente e o servidor
        self.stub = pb2_grpc.TestsRPCStub(self.channel)

    # Chamada do método RPC responsável por receber como parâmetro e ter como valor de retorno uma string
    def get_url(self, message):
        message = pb2.Message(message=message)
        return self.stub.GetServerResponse(message)

    # Chamada do método RPC responsável por receber como parâmetro e ter como valor de retorno void/mensagem vazia
    def get_void(self):
        request = Empty() # Create an empty request object
        return self.stub.GetsVoid(request)
    
    # Chamada do método RPC responsável por receber como parâmetro e ter como valor de retorno um long
    def get_long(self, number):
        request = pb2.parameters(number=number)
        response = self.stub.GetsLong(request)
        return response.result
    
    #Chamada do método RPC responsável por receber como parametros 8 valores do tipo long e retornar um valor do tipo long
    def get_8long(self, values):
        request = pb2.parameters(long_values=values)
        response = self.stub.GetsEightLongs(request)
        return response.result
    
    # Chamada do método RPC responsável por receber como parametro um tipo complexo(Classe) e retornar um valor de tipo complexo(Classe)
    def get_class(self,values):
        instance = pb2.MyClass(value=values)
        request = pb2.ProcessClassRequest(instance=instance)
        response = self.stub.ProcessClass(request)
        return response.result


if __name__ == '__main__':
    client = TesterClient()
    # Loop responsável por receber e printar os casos testes
    while True:
        op = int(input("Digite a operação: "))
        if(op == 0):
            print('Saindo')
            break
        elif(op == 1):
            for i in range(10):
                start = time.perf_counter()
                result = client.get_void()
                end = time.perf_counter()
                elapsed_time = end - start
                print(f'{elapsed_time:.9f}'.replace('.', ','))
        elif(op == 2):
            for i in range(10):
                start = time.perf_counter()
                result = client.get_long(2**10)
                end = time.perf_counter()
                elapsed_time = end - start
                print(f'{elapsed_time:.9f}'.replace('.', ','))
        elif(op == 3):
            values = [2**10,2**10,2**10,2**10,2**10,2**10,2**10,2**10]
            for i in range(10):
                start = time.perf_counter()
                result = client.get_8long(values)
                end = time.perf_counter()
                elapsed_time = end - start
                print(f'{elapsed_time:.9f}'.replace('.', ','))
        elif(op == 4):
            char = "A"
            powers = [1,2,4,8,16,32,64,128,256,512]
            for i in range(len(powers)):
                start = time.perf_counter()
                result = client.get_url(char*powers[i])
                end = time.perf_counter()
                elapsed_time = end - start
                print(f'{elapsed_time:.9f}'.replace('.', ','))
        elif(op == 5):
            for i in range(10):
                start = time.perf_counter()
                result = client.get_class(10)
                end = time.perf_counter()
                elapsed_time = end - start
                print(f'{elapsed_time:.9f}'.replace('.', ','))
        else:
            break