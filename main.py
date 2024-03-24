import socket
import hashlib
import streamlit as st

def server_pgm():
    host = socket.gethostname()
    port = 9997
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    st.success(f"🚀 **Connection from:** {address}")

    data = conn.recv(8192)
    st.info("Received data from client.")
    st.info(f"Length of data: {len(data)} bytes")

    # Save the received data to a file
    with open('output/ClientToServer.txt', 'wb') as file:
        file.write(data)

    st.success("📥 Saved received data to 'ClientToServer.txt'")

    # Send acknowledgment to the client
    conn.send("Data Received".encode())
    st.success("📤 Acknowledgment sent to client")

    # Receive client's request
    request = conn.recv(1024).decode()

    # Check if the client is requesting the data
    if request == "REQUEST_DATA":
        st.info("Client requested the data.")
        with open('output/ClientToServer.txt', 'rb') as file:
            file_data = file.read()

        # Send the content of the 'ReceivedFile.txt' to the client
        conn.send(file_data)
        st.success("📤 Sent 'ClientToServer.txt' content to the client")

    conn.close()

def main():
    st.title("File Transfer Server")
    st.write("Waiting for connection...")

    if st.button("Start Server"):
        server_pgm()
        st.success("🛑 Server closed.")

if __name__ == '__main__':
    main()
