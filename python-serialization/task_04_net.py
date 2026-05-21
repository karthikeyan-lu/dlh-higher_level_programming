#!/usr/bin/env python3
"""Client-server application with JSON serialization."""

import socket
import json


def start_server(host="127.0.0.1", port=12345):
    """Start a server, receive JSON data, deserialize it, and print it."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((host, port))
        server_socket.listen(1)

        connection, address = server_socket.accept()

        with connection:
            data = connection.recv(4096)

            dictionary = json.loads(data.decode("utf-8"))

            print("Received Dictionary from Client:")
            print(dictionary)

        server_socket.close()

    except Exception as e:
        print(f"Server error: {e}")


def send_data(data, host="127.0.0.1", port=12345):
    """Serialize a dictionary and send it to the server."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        serialized_data = json.dumps(data).encode("utf-8")

        client_socket.connect((host, port))
        client_socket.sendall(serialized_data)

        client_socket.close()

    except Exception as e:
        print(f"Client error: {e}")
