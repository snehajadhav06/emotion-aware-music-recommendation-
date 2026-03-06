import speech_recognition as sr

def record_voice():

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("Adjusting for background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Listening... Speak now!")

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

        text = recognizer.recognize_google(audio)

        return text

    except sr.WaitTimeoutError:
        return None

    except sr.UnknownValueError:
        return None

    except sr.RequestError:
        return None

