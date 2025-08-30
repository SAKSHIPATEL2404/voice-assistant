📌 Overview

This project is a simple Voice Assistant built using Python and the Vosk Speech Recognition API.
It can listen to your voice through a microphone, recognize speech, and perform basic tasks.


✨ Features

🎤 Speech-to-Text using Vosk Model

🔊 Text-to-Speech response

⚡ Real-time audio processing

📚 Easy to extend with custom commands (e.g., weather, opening apps, etc.)


🛠 Technologies Used

Python 3

Vosk Speech Recognition

PyAudio (for microphone input)

gTTS / pyttsx3 (for text-to-speech, optional)


📂 Project Structure

voice-assistant/
│
├── main.py                # Core script
├── vosk-model-small-en-us-0.15/   # Vosk model files
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

## 🚀 Installation  

1. *Clone the repository*  
```bash
git clone https://github.com/SAKSHIPATEL1204/voice-assistance-python.git
cd voice-assistance-python

2. Create virtual environment (recommended)

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

3. Install dependencies
pip install -r requirements.txt

Run the main script:

python main.py

Speak into your microphone 🎤 and the assistant will recognize your voice and respond.


---

📌 Future Enhancements

🌐 Add weather and news API integration

📂 Open applications via voice commands

🧠 Add Natural Language Understanding (NLU)

💡 Improve real-time response



---

👩‍💻 Author

Developed by Sakshi Patel.....
