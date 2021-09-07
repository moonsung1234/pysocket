
class Event :
    def __init__(self) :
        self.events = {}
    
    def __addEvent(self, event_name, callback) :
        self.events[event_name] = callback

    def on(self, event_name, callback) :
        # same to addEvent method
        self.__addEvent(event_name, callback)

    def __callEvent(self, event_name, args=None) :
        return self.events[event_name](*args)

    def emit(self, event_name, args=None) :
        _args = args

        # same to callEvent method
        return self.__callEvent(event_name, args=_args)

    def removeEvent(self, event_name) :
        del self.events[event_name]

    def removeAllEvent(self) :
        self.events = {}