class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = None
        self.calls = dict()

    def __getattr__(self, attr):
        if attr in dir(self._obj):
            self.last_invoked = attr
            self.calls[attr] = self.calls.get(attr, 0) + 1
            return getattr(self._obj, attr)
        raise Exception("No Such Method")

    def last_invoked_method(self):
        if self.last_invoked:
            return self.last_invoked
        raise Exception("No Method Is Invoked")

    def count_of_calls(self, method_name):
        return self.calls.get(method_name, 0)

    def was_called(self, method_name):
        if method_name in self.calls.keys():
            return True
        else:
            return False


class Radio:
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on


radio = Radio()
radio_proxy = Proxy(radio)
radio_proxy.set_channel(95)
radio_proxy.power()
print(radio.get_channel())
