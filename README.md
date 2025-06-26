# 🗣️ Jcodes Text to Speech App

A simple GUI-based Text-to-Speech (TTS) Python application using `tkinter` for the interface and `pyttsx3` for voice output. Type text into the input field and click the "Speak" button to hear your words spoken aloud.

## 📦 Features

- 🔊 Converts written text to speech
- 🧑‍💻 User-friendly interface built with `tkinter`
- 🎛️ Compact and responsive design
- 🎤 Uses `pyttsx3` for offline speech synthesis

## 🛠️ Technologies Used

- Python 🐍
- `tkinter` - for GUI
- `pyttsx3` - text-to-speech conversion

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed (preferably 3.x).  
Install the required Python library using pip:

```bash
pip install pyttsx3

Running the App
Clone this repository or download the code.

Run the Python script:
  python your_script_name.py
(Replace your_script_name.py with the actual file name.)

📁 Project Structure
text-to-speech-app/
│
├── tts_app.py           # Main Python script
└── README.md            # Project documentation

🤖 How It Works
The user inputs text into the entry box.

Clicking the "Speak" button triggers the speaknow() function.

pyttsx3 reads the text aloud using the system's default voice engine.

📌 Notes
This app works offline — no internet connection required.

You can customize the voice and rate by modifying pyttsx3 settings.

🙌 Credits
Built by jcodes

📝 License
This project is licensed under the MIT License.
