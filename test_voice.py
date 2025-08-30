import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed thoda tez
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice (agar available)
engine.say("Test voice output. Agar aapko awaaz sunai de rahi hai, to pyttsx3 sahi kaam kar raha hai.")
engine.runAndWait()
