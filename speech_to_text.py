import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 You Speak...")
        r.adjust_for_ambient_noise(source)  # helps reduce background noise
        audio = r.listen(source)

    try:
        voice_data = r.recognize_google(audio, language="en-IN")  # you can change language
        print("You said:", voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Could not understand audio ❌")
    except sr.RequestError:
        print("Could not request results, check your internet connection 🌐")

speech_to_text()
