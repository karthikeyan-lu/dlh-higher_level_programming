#!/usr/bin/env python3
"""Client-server application with JSON serialization."""

import json
import socket


def start_server(host="127.0.0.1", port=12345):
    """Start server, receive JSON data, deserialize, and print dictionary."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)

        connection, _ = server_socket.accept()

        with connection:
            data = connection.recv(4096)
            dictionary = json.loads(data.decode("utf-8"))

            print("Received Dictionary from Client:")
            print(dictionary)


def send_data(data, host="127.0.0.1", port=12345):
    """Serialize dictionary and send it to server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        serialized_data = json.dumps(data).encode("utf-8")
        client_socket.sendall(serialized_data)
