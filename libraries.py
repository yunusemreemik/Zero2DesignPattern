# # Using itertools for Advanced Iteration
# import itertools

# # Infinite cycle of elements
# cycle = itertools.cycle([1, 2, 3])
# for _ in range(2):
#     print(next(cycle))  # Outputs: 1, 2, 3, 1, 2, 3, ...

# # Using functools for Advanced Functions
# import functools

# # Partial function application
# multiply_by_2 = functools.partial(lambda x, y: x * y, 2)
# result = multiply_by_2(5)
# print(result)  # Output: 10

# # Using asyncio for Concurrent Programming
# import asyncio

# async def my_coroutine():
#     print("Coroutine Started")
#     await asyncio.sleep(1)
#     print("Coroutine Ended")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(my_coroutine())

# Using socket for Network Programming
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))
server_socket.listen(1)
client_socket, addr = server_socket.accept()
print("Connection established with:", addr)