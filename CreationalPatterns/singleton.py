class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance

singleton1 = Singleton()
singleton1.value = 10
print(singleton1.value)  # Output: 10

singleton2 = Singleton()
singleton2.value = 15
print(singleton1.value)  # Output: 10 (Same instance as singleton1)