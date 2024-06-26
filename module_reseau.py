import socket

class Reseau:
    """Classe réseau faisant le lien entre le programme et minetest"""
    def __init__(self):
        self.ma_socket = None

    def connect_to(self, ip, port):
        """"Connection au serveur désigné, par défaut local(127.0.0.1)"""
        self.ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ma_socket.connect((ip, port))

    def disconnect(self):
        """Permet la déconnection"""
        self.ma_socket.close()

    def chat_post(self, message: str):
        """Poste des messages dans le chat minetest"""
        requete = "chat.post("+message+")\n"
        self.ma_socket.send(requete.encode())

    def world_set_block(self, x, y, z, block_data):
        """Pose un block defini en une coordonnée définie"""
        requete = f"world.setBlock({x},{y},{z}, 35,{block_data})\n"
        self.ma_socket.send(requete.encode())

    def world_set_blocks(self, x1, y1, z1, x2, y2, z2, block_data):
        """Pose un cube de blocks"""
        requete = f"world.setBlocks({x1},{y1},{z1},{x2},{y2},{z2}, 35,{block_data})\n"
        self.ma_socket.send(requete.encode())
    

if __name__ == '__main__':
    test = Reseau()
    test.connect_to()
    test.chat_post("L")
    test.world_set_block(0, 10, 0, 0)
    test.world_set_blocks(10, 10, 10, -10, -10, -10, 11)
    test.disconnect()
    