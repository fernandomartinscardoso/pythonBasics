"""Bluetooth terminal chat for Ubuntu using Python's native socket support."""

import socket
import sys
import threading


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[Connection closed by remote device]")
                break
            print(f"\n[Received]: {data.decode('utf-8').strip()}")
            print("You: ", end="", flush=True)
        except OSError:
            break


def run_server(port=1):
    server_sock = socket.socket(
        socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
    )
    server_sock.bind((socket.BDADDR_ANY, port))
    server_sock.listen(1)
    print(f"Server listening on channel {port}... Waiting for connection.")
    
    conn, addr = server_sock.accept()
    print(f"Connected to {addr}")
    return server_sock, conn


def run_client(target_address, port=1):
    client_sock = socket.socket(
        socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
    )
    print(f"Connecting to {target_address} on channel {port}...")
    client_sock.connect((target_address, port))
    print("Connected successfully!")
    return client_sock


def main():
    if not hasattr(socket, "AF_BLUETOOTH"):
        print("Bluetooth sockets are not supported on this platform.")
        sys.exit(1)

    role = input("Start as (S)erver or (C)lient? [s/c]: ").strip().lower()
    
    conn = None
    server_sock = None

    try:
        if role.startswith("s"):
            port_input = input("Enter channel/port [default: 1]: ").strip()
            port = int(port_input) if port_input else 1
            server_sock, conn = run_server(port)
        elif role.startswith("c"):
            target_mac = input("Enter remote Bluetooth MAC address (XX:XX:XX:XX:XX:XX): ").strip()
            if not target_mac:
                print("Bluetooth address is required.")
                sys.exit(1)
            port_input = input("Enter channel/port [default: 1]: ").strip()
            port = int(port_input) if port_input else 1
            conn = run_client(target_mac, port)
        else:
            print("Invalid choice.")
            sys.exit(1)

        recv_thread = threading.Thread(target=receive_messages, args=(conn,), daemon=True)
        recv_thread.start()

        print("\n--- Chat session started (type 'exit' or press Ctrl+C to quit) ---")
        while True:
            msg = input("You: ")
            if msg.strip().lower() == "exit":
                break
            conn.sendall((msg + "\n").encode("utf-8"))

    except KeyboardInterrupt:
        print("\nExiting chat...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
        if server_sock:
            server_sock.close()
        print("Disconnected.")


if __name__ == "__main__":
    main()

