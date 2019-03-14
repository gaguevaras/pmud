import selectors
import telnetlib

import sys


REQUEST = 1001
RESPONSE = 1002


class Mud:
    def __init__(self, telnet):
        self.tn = telnet
        self.__input_observers = []
        self.__output_observers = []

    def register_input_observer(self, observer):
        self.__input_observers.append(observer)

    def register_output_observer(self, observer):
        self.__output_observers.append(observer)

    def notify_input_observers(self, *args, **kwargs):
        responses = []
        for observer in self.__input_observers:
            responses.append(observer.notify(self, *args, **kwargs))
        return responses

    def notify_output_observers(self, *args, **kwargs):
        responses = []
        for observer in self.__output_observers:
            responses.append(observer.notify(self, *args, **kwargs))
        return responses

    def mud_interact(self):
        if sys.platform == "win32":
            self.tn.mt_interact()
            return
        with telnetlib._TelnetSelector() as selector:
            selector.register(self.tn, selectors.EVENT_READ)
            selector.register(sys.stdin, selectors.EVENT_READ)

            while True:
                for key, events in selector.select():
                    if key.fileobj is self.tn:
                        try:
                            text = self.tn.read_very_eager()
                        except EOFError:
                            print('*** Connection closed by remote host ***')
                            return
                        if text:
                            self.receive(text)
                    elif key.fileobj is sys.stdin:
                        line = sys.stdin.readline().encode('ascii')
                        if not line:
                            return
                        self.send(line)

    # Both the send and receive texts are subject to observation
    def send(self, line):
        # Determine if user is manually triggering an action
        if True not in self.notify_input_observers(line=line.decode()):
            self.tn.write(line)

    def receive(self, text):
        # Determine if text triggers any actions
        
        sys.stdout.write(text.decode('ascii'))
        sys.stdout.flush()

