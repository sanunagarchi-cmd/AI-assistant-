import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()

    # set voice speed (default ~200)
    engine.setProperty('rate', 170)

    # optional: change volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()


# test
spoken = text_to_speech("Hello Seenu")
print("Returned:", spoken)
