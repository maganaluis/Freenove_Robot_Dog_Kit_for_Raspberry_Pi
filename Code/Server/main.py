# -*- coding: utf-8 -*-
from Server import *
import atexit

class Runner:
    def __init__(self):
        self.server=Server()

    def run(self):
        self.server.turn_on_server()
        self.server.tcp_flag=True
        self.video=threading.Thread(target=self.server.transmission_video)
        self.video.start()
        self.instruction=threading.Thread(target=self.server.receive_instruction)
        self.instruction.start()

    @atexit.register
    def cleanup(self):
        try:
            stop_thread(self.video)
            stop_thread(self.instruction)
        except:
            pass
        try:
            self.server.server_socket.shutdown(2)
            self.server.server_socket1.shutdown(2)
            self.server.turn_off_server()
        except:
            pass
        os._exit(0)
        
if __name__ == '__main__':
    runner = Runner()
    runner.run()
