# Basic Scripts

This directory contains standalone Python utility scripts for system interaction, text-to-speech, and device communication.

---

## 📡 Bluetooth Terminal Chat (`bluetooth_chat.py`)

A bidirectional, terminal-based chat application designed to run on Ubuntu Linux using Python's native `socket` module. It communicates over Bluetooth RFCOMM channels using background threading for real-time messaging.

### 📋 Prerequisites

Before running the script on Ubuntu, ensure the BlueZ Bluetooth stack is installed and active:

```bash
sudo apt update
sudo apt install bluez
sudo systemctl start bluetooth
```

#### Adapter Configuration
Ensure your Bluetooth adapter is powered on and discoverable:

```bash
# Power on Bluetooth adapter
bluetoothctl power on

# Make the device discoverable (necessary for Server mode)
bluetoothctl discoverable on
```

### ⚙️ How It Works

1. **Native Bluetooth Sockets:** Uses Python's built-in `socket.AF_BLUETOOTH` and `socket.BTPROTO_RFCOMM` constants (no extra third-party libraries required on Linux).
2. **Role Selection:**
   - **Server Mode:** Binds to an RFCOMM port/channel (default: `1`) on `BDADDR_ANY` (`00:00:00:00:00:00`) and waits for an incoming connection.
   - **Client Mode:** Connects to a target device's Bluetooth MAC address on the specified channel.
3. **Concurrent 2-Way Messaging:** Spawns a daemon `threading.Thread` to receive and display incoming messages asynchronously while the main thread waits for user text input.

### 🚀 Usage

Run the script from your terminal:

```bash
python basicScripts/bluetooth_chat.py
```

#### Step-by-Step Example

1. **Choose Role:**
   ```text
   Start as (S)erver or (C)lient? [s/c]: s
   Enter channel/port [default: 1]: 1
   Server listening on channel 1... Waiting for connection.
   ```

2. **Connect from Client Device:**
   On the client machine:
   ```text
   Start as (S)erver or (C)lient? [s/c]: c
   Enter remote Bluetooth MAC address (XX:XX:XX:XX:XX:XX): 00:11:22:33:44:55
   Enter channel/port [default: 1]: 1
   Connecting to 00:11:22:33:44:55 on channel 1...
   Connected successfully!
   ```

3. **Chat:**
   ```text
   --- Chat session started (type 'exit' or press Ctrl+C to quit) ---
   You: Hello from Server!
   
   [Received]: Hi from Client!
   You: 
   ```

To end the session, type `exit` or press `Ctrl+C`.

---

## 🕒 Speak the Current Time (`say_time.py`)

Prints the current local date and time, then reads it aloud using the cross-platform `pyttsx3` text-to-speech library.

### 📋 Requirements

Install the Python dependency from the repository root:

```bash
python -m pip install pyttsx3
```

On Ubuntu, `pyttsx3` also needs a speech engine. Install eSpeak NG if one is not already available:

```bash
sudo apt update
sudo apt install espeak-ng
```

### 🚀 Usage

From the repository root, run:

```bash
python basicScripts/say_time.py
```

The script prints a date and time such as `06 30 PM on Saturday, October 17, 2026`, then speaks the same text. The displayed and spoken time comes from the computer's local clock.

---

## 🗣️ Speak User-Provided Text (`speak.py`)

Prompts for a line of text in the terminal and reads it aloud using the cross-platform `pyttsx3` text-to-speech library. Blank input is ignored.

### 📋 Requirements

Install the Python dependency from the repository root:

```bash
python -m pip install pyttsx3
```

On Ubuntu, install a speech engine if one is not already available:

```bash
sudo apt update
sudo apt install espeak-ng
```

### 🚀 Usage

From the repository root, run:

```bash
python basicScripts/speak.py
```

Enter the text to be spoken when prompted.

---

## 📷 Take a Picture (`take_picture.py`)

Opens a live preview from the default webcam and saves a snapshot as `qpython.jpg` in the current working directory.

### 📋 Requirements

Install the Python dependency from the repository root:

```bash
python -m pip install opencv-python
```

The Ubuntu user running the script must have permission to access the webcam. Connect the camera and close other applications that may be using it.

### 🚀 Usage

From the repository root, run:

```bash
python basicScripts/take_picture.py
```

In the preview window, press **Space** to capture the current frame, or **Q** or **Esc** to cancel. The script prints the full path of the saved image.
