# Jarvis Voice-Enabled Chatbot

## Project Overview

Jarvis is a voice-enabled chatbot developed using Python. The chatbot accepts both keyboard and microphone input, converts speech to text, processes user requests, and responds through both text and speech. It also maintains a conversation log with timestamps.

This project was developed as part of the Daily Task assignment: **"Why Use Jarvis? Build One."**

---

## Features

### Dual Input Support

* Accepts typed input from the keyboard.
* Accepts voice input through the microphone.

### Speech-to-Text Conversion

* Converts spoken words into text using SpeechRecognition.

### Dual Output

* Displays responses in the console.
* Speaks responses aloud using pyttsx3.

### Conversation Logging

* Saves the complete conversation with timestamps in a text file.

### Additional Features

* Current date retrieval.
* Current time retrieval.
* Basic calculator functionality.
* Time-based greetings.

---

## Technologies Used

* Python 3.12
* SpeechRecognition
* PyAudio
* pyttsx3
* datetime

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-link>
cd jarvis-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

---

## How to Run

```bash
python chatbot.py
```

---

## Usage

1. Run the program.
2. Select:

   * 1 for Text Input
   * 2 for Voice Input
   * Type 'bye' to exit.
3. Enter or speak your query.
4. Jarvis processes the request.
5. The response is:

   * Displayed on the console.
   * Spoken aloud.
6. The conversation is automatically saved in `conversation_log.txt`.

---

## Project Structure

```text
jarvis-chatbot/
│
├── chatbot.py
├── conversation_log.txt 
└── README.md
```

---

## Example Commands

* Hello
* What is the time?
* What is today's date?
* Calculate 25 * 4
* What is your name?
* Bye

---

## Challenges Faced

Initially, Python 3.14 caused compatibility issues with PyAudio installation. To resolve this, Python 3.12 was installed and a virtual environment was created. After installing the required libraries, the microphone and text-to-speech features worked successfully.

---

## Author

Developed as part of the Daily Task Assignment on 18/06/2026.
