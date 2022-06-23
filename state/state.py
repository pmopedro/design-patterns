from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):

    @abstractmethod
    def do(self):
        pass

class StartState(State):
    def do(self):
        print("Switching TV on")

class StopState(State):
    def do(self):
        print("Switching TV off")

class TV(State):

    def __init__(self):
        self.state=None

    def getState(self): 
        return self.state

    def setState(self,state):
        self.state = state

    def do(self):
        self.state.do()

context = TV()
context.getState()
start = StartState()
stop = StopState()

context.setState(stop)
context.do()
print(context.getState())


context.setState(start)
context.do()
print(context.getState())
