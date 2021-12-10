class Network:
    __queue = []

    def send(self, message):
        self.__queue.append(message)

    def receive(self):
        return self.__queue.pop(0)
