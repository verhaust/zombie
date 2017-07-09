import asyncio
import time

class Player(object):

    def __init__(self, connection_info):
        self.host = connection_info[0]
        self.port = connection_info[1]
        self.name = ""
        self.history = []
        self.state = 0
        self.commands_to_process = []

    def process_commands(self):
        for command in self.commands_to_process:
            print(time.time())
            print(command)
        
def intro_message():
    intro = "Welcome to ZombieMUD\n"
    return intro

class Connection(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.player = Player(peername)
        self.transport = transport
        self.transport.write(intro_message().encode())
        self.transport.write("Name: ".encode())
        self.buffer = "" 

    def attach_to_buffer(self, message):
        if "\n" in message:
            commands = message.split("\n")
            commands[0] = self.buffer + commands[0]
            self.buffer = commands[-1]
            commands.pop()
            self.player.commands_to_process += commands
        else:
            self.buffer += message
        
    def data_received(self, data):
        message = data.decode()
        self.attach_to_buffer(message)
        self.player.process_commands()

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
#coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
coro = loop.create_server(Connection, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
