import webbrowser
import speech_recognition as sr
import pyttsx3
import motivationLibrary
import box
import requests
from groq import Groq

recognizer = sr.Recognizer()

newsapi = box.newsapikey     # tumhari api key "newsapi" weebsite se leko idhar daaliyo
GROQ_API_KEY = box.groqkey

client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def aiProcess(command):
    """Processes unhandled commands through Groq's open model."""
    try:
        response = client.chat.completions.create(
            # Standard high-speed active model on Groq
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You are JARVIS, a helpful voice assistant. Keep answers short and concise (maximum 1 to 2 sentences) so they are easy to speak out loud.",
                },
                {"role": "user", "content": command},
            ],
            temperature=0.7,
            max_tokens=150,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Groq API Error: {e}")
        return "Sorry, I could not process that request with Groq."

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")

    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com/feed/")

    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "open gemini" in c.lower():
        speak("Opening gemini")
        webbrowser.open("https://gemini.google.com/app")

    elif c.lower().startswith("play"):
        motiv = c.lower().split(" ")[1]
        link = motivationLibrary.motives[motiv]
        webbrowser.open(link)

    elif "news" in c.lower():
        print("heard : ", c)
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}', headers=headers)

        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles[:5]:
                print(article['title'])
                speak(article['title'])

    #GROQ ab aata
    else:
        print(c)
        output = aiProcess(c)
        speak(output)
        #print(output)

if __name__ == "__main__":
    speak(" Intializing Jarvis ....")

    while True:

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("You said:", repr(word))  #repr()shows actual string, including spaces and hidden characters.

            if "jarvis" in word.lower():
                speak("Yes sir")

                # listen for command
                with sr.Microphone() as source:
                    print("JARVIS active ...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                    command = recognizer.recognize_google(audio)

                    print(command)
                    processCommand(command)

        except Exception as e:
            print(f"Error {e}")
