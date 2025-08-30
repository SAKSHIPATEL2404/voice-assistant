import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import pywhatkit
import requests
import smtplib
import datetime
import os

# -------------------
# 1. Text to Speech
# -------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # speed
engine.setProperty("volume", 1.0)  # volume

def speak(text):
    voices = engine.getProperty('voices')
    for v in voices:
        if 'female' in v.name.lower():
            engine.setProperty('voice', v.id)
            break
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# -------------------
# 2. Listen Function
# -------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# -------------------
# 3. Weather Function
# -------------------
def get_weather(city):
    api_key = "61ecd8e127cb174073b3ba37bd8c0701"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response["cod"] == 200:
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            return f"The temperature in {city} is {temp}°C with {desc}."
        else:
            return "City not found."
    except:
        return "Sorry, I couldn't fetch the weather right now."

# -------------------
# 4. Email Function
# -------------------
def send_email(to, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_app_password")  # ⚠ Replace with your Gmail + App Password
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail("your_email@gmail.com", to, message)
        server.quit()
        return "Email successfully sent."
    except Exception as e:
        return f"Error: {e}"

# -------------------
# 5. WhatsApp Function
# -------------------
def send_whatsapp(number, message):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # 2 minute baad bhejega
    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        return "WhatsApp message scheduled successfully."
    except Exception as e:
        return f"Error: {e}"

# -------------------
# 6. Main Assistant
# -------------------
def main():
    speak("Hello Sakshi! I am your AI Voice Assistant. How can I help you?")

    while True:
        query = listen()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
            speak(result)

        elif "search" in query:
            search_term = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            speak(f"Here are the search results for {search_term}")

        elif "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif "open google" in query:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif "weather" in query:
            speak("Which city?")
            city = listen()
            weather = get_weather(city)
            speak(weather)

        elif "send email" in query:
            speak("Who is the recipient?")
            to = input("Enter email: ")  # 👈 for testing
            speak("What is the subject?")
            subject = listen()
            speak("What should I say?")
            body = listen()
            result = send_email(to, subject, body)
            speak(result)

        elif "send whatsapp" in query:
            speak("Tell me the number with country code, like +91...")
            number = input("Enter number: ")  # 👈 for testing
            speak("What should I send?")
            message = listen()
            result = send_whatsapp(number, message)
            speak(result)

        elif "exit" in query or "stop" in query:
            speak("Goodbye Sakshi! Have a nice day.")
            break

if __name__ == "__main__":
    main()

