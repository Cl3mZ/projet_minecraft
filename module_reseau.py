import socket

class Reseau:
    def __init__(self, x, y, z, block_id, block_data):
        self.ma_socket = None
        self.x = x
        self.y = y
        self.z = z
        self.block_id = block_id
        self.block_data = block_data

    def connect_to(self):
        self.ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ma_socket.connect(("127.0.0.1", 4711))

    def disconnect(self):
        self.ma_socket.close()

    def chat_post(self, message: str):
        requete = "chat.post("+message+")\n"
        self.ma_socket.send(requete.encode())

    def world_set_block(self):
        requete = f"world.setBlock({self.x},{self.y},{self.z},{self.block_id},{self.block_data})\n"
        print(requete)
        self.ma_socket.send(requete.encode())

    #def world_set_blocks(self, x1 :int, y1: int, z1: int, x2 :int, y2: int, z2: int, block_id: int, block_data: int):

if __name__ == '__main__':
    test = Reseau(100, 100, 100, 35, 15)
    test.connect_to()
    #test.chat_post("L")
    test.world_set_block('test')
    