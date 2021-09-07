
import pickle

class Packet :
    def __init__(self, packet_name, data) :
        self.packet_name = packet_name
        self.data = data

    def encode(self) :
        return pickle.dumps(self)

    @classmethod
    def decode(self, data) :
        return pickle.loads(data)