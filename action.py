import speech_to_text
import datetime
import webbrowser
import text_to_speech


def act(data):
    if not data:   # handles None or empty string
        user_data = ""
    else:
        user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.tts("My name is Virtual Assistant")
        return "My name is Virtual Assistant"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.tts("Hey sir, aap kaise hain?")
        return "Hey sir, aap kaise hain?"

    elif "good morning" in user_data:
        text_to_speech.tts("Good morning sir")
        return "Good morning sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = current_time.strftime("The time is %H hour and %M minutes")
        text_to_speech.tts(Time)
        return "The time is %H hour and %M minutes"

    elif "shutdown" in user_data:
        text_to_speech.tts("Ok boss, shutting down")
        return "Ok boss, shutting down"

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.tts("Spotify is ready for you")
        return "Spotify is ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.tts("YouTube has opened now")
        return "YouTube has opened now"

    elif "open apunkagames" in user_data:
        webbrowser.open("https://www.apunkagames.com/")
        text_to_speech.tts("Now you can download games")
        return "Now you can download games"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.tts("Google has open now")
        return "Google have opened now"

    else:
        text_to_speech.tts("I am not able to understand sir")
        return "I am not able to understand sir"
