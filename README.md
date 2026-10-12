# JARVIS – AI-Powered Voice Assistant

JARVIS is a Python-based voice assistant that listens to voice commands, performs useful tasks, fetches the latest headlines, and answers general questions using a Large Language Model (LLM) through the Groq API.

The project combines speech recognition, text-to-speech, web automation, and AI-powered responses to create a simple, interactive voice assistant.

## Features

- **Voice Activation:** Listens for the keyword `Jarvis` before processing commands.
- **Text-to-Speech:** Responds verbally using `pyttsx3`.
- **Speech Recognition:** Converts spoken commands into text using Google Speech Recognition.
- **Website Automation:** Opens Google, LinkedIn, YouTube, and Gemini through voice commands.
- **AI-Powered Responses:** Uses the Groq API with the `openai/gpt-oss-20b` model to answer general questions.
- **Latest News:** Fetches and reads the top five US headlines using the NewsAPI.
- **Motivational Content:** Opens motivational content based on predefined commands stored in a custom Python module.
- **API Key Protection:** Keeps API credentials in a separate `box.py` file, which should be excluded from version control using `.gitignore`.

## Technologies Used

- Python
- SpeechRecognition
- PyAudio (microphone input dependency)
- pyttsx3
- Groq API
- NewsAPI
- Requests
- Webbrowser module

## Project Structure

```text
JARVIS/
├── main.py                 # Main voice assistant program
├── motivationLibrary.py    # Predefined motivational content and links
├── .gitignore              # Excludes sensitive and unnecessary files
├── README.md               # Project documentation
└── box.py                  # Local API credentials (not uploaded to GitHub)
```

*Note: Replace `main.py` with the actual filename of your main Python script if it is different.*

## Prerequisites

- Python 3.9 or a compatible version supported by the installed dependencies.
- A working microphone.
- An internet connection.
- A NewsAPI API key.
- A Groq API key.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the repository URL with your GitHub repository URL.

### 2. Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 requests groq pyaudio
```

Depending on your operating system, PyAudio may require additional setup.

### 3. Configure API Keys

Create a local file named `box.py` in the project directory:

```python
newsapikey = "YOUR_NEWSAPI_KEY"
groqkey = "YOUR_GROQ_API_KEY"
```

Replace the placeholders with your own API keys.


### 4. Run the Assistant

Run the main Python file:

```bash
python main.py
```

Say **"Jarvis"** when the assistant is listening, then speak your command.

## Example Voice Commands

| Voice command | Action |
|---|---|
| "Jarvis, open Google" | Opens Google |
| "Jarvis, open LinkedIn" | Opens LinkedIn |
| "Jarvis, open YouTube" | Opens YouTube |
| "Jarvis, open Gemini" | Opens Google Gemini |
| "Jarvis, news" | Reads the latest US headlines |
| "Jarvis, play [name]" | Opens the matching motivational link |
| "Jarvis, what is artificial intelligence?" | Generates an AI response |

For motivational commands, the requested name must exist as a key in `motivationLibrary.motives`.

## How It Works

1. The program continuously listens through the microphone.
2. Google Speech Recognition converts the detected speech into text.
3. The assistant checks whether the wake word "Jarvis" is present.
4. Once activated, it listens for the user's command.
5. The command processor identifies supported actions.
6. For general questions, the Groq API generates a response.
7. The `pyttsx3` engine converts the response into speech.

## Limitations

- Speech recognition requires an internet connection when using Google's recognition service.
- Background noise may affect command detection.
- The current implementation supports a limited set of predefined website commands.
- News retrieval depends on NewsAPI access, availability, and plan restrictions.
- AI responses require a valid Groq API key and an available model.
- The assistant continuously listens until the program is stopped manually.

## Future Enhancements

- Add support for more applications and system commands.
- Introduce a graphical user interface.
- Add error handling for unsupported or incomplete voice commands.
- Improve wake-word detection and background-noise handling.
- Store API credentials using environment variables.
- Add reminders, weather updates, and other useful assistant features.

## Learning Outcomes

This project demonstrates practical experience with Python modules, APIs, speech recognition, text-to-speech systems, conditional logic, exception handling, and integrating an LLM into an application.

## Author

Syed Hammad

Computer Science and Engineer – Artificial Intelligence and Machine Learning

## License

This project is available for educational and personal learning purposes. Add a formal open-source license if you intend to specify permissions for reuse and redistribution.
