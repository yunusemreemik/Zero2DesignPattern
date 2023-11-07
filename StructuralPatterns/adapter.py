# Step 1: Adaptee (Incompatible Interface)
class EuropeanSocket:
    def power_on(self):
        return "Power is connected using European Socket"

# Step 2: Target Interface (Expected by the Client)
class USASocketInterface:
    def power_on(self):
        pass

# Step 3: Adapter (Adapting EuropeanSocket to USASocketInterface)
class Adapter(USASocketInterface):
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def power_on(self):
        return f"Adapter: {self.european_socket.power_on()} converted to USA Socket"

# Step 4: Client Code (Using the Target Interface)
class Laptop:
    def __init__(self, socket):
        self.socket = socket

    def charge(self):
        return self.socket.power_on()

# Step 5: Client Usage
european_socket = EuropeanSocket()
adapter = Adapter(european_socket)
laptop = Laptop(adapter)

print(laptop.charge())  # Output: "Adapter: Power is connected using European Socket converted to USA Socket"
