# Step 1: Complex Subsystem Classes
class CPU:
    def freeze(self):
        print("Freezing CPU")

    def jump(self, position):
        print(f"Jumping to address {position}")

class Memory:
    def load(self, position, data):
        print(f"Loading data '{data}' to memory address {position}")

class HardDrive:
    def read(self, lba, size):
        print(f"Reading {size} bytes from Hard Drive at LBA {lba}")

# Step 2: Facade Class
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", "Bootstrap Loader")
        self.hard_drive.read("0x01", 1024)
        self.cpu.jump("0x10")
        print("Computer started successfully.")

# Step 3: Client Code Using Facade
class User:
    def __init__(self, computer):
        self.computer = computer

    def power_on(self):
        print("User pressing power button.")
        self.computer.start()

# Step 4: Client Usage
computer_facade = ComputerFacade()
user = User(computer_facade)
user.power_on()
