# File Transfer Application :)

📁 **Description:**

This is a simple client-server file transfer application built in Python. It allows clients to upload files to the server and download files from the server. The server performs Merkle tree integrity checking.
🚀 **Features:**

- **Server Side:**
  - Waits for incoming connections from clients.
  - Receives files from clients and saves them.
  - Sends files to clients upon request.
  - Performs Merkle tree integrity checks.

- **Client Side:**
  - Connects to the server.
  - Encrypts and sends files to the server.
  - Requests files from the server and verifies integrity.

📝 **Dependencies:**

- Python 3.11.4
- Socket library
- hashlib library
- streamlit 1.35.0 
