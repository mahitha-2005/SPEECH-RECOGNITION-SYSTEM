import speech_recognition as sr

def transcribe_audio(audio_file, engine='google'):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            print("Listening...")
            audio = recognizer.record(source)

        print("Transcribing...")

        if engine.lower() == 'google':
            text = recognizer.recognize_google(audio)
        elif engine.lower() == 'sphinx':
            # Uses CMU Sphinx offline recognition, requires pocketsphinx installed
            text = recognizer.recognize_sphinx(audio)
        else:
            print(f"Unsupported recognition engine: {engine}")
            return None

        print("Transcription:\n", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from the recognition service; {e}")
    except FileNotFoundError:
        print("The audio file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to your audio file (.wav): ")
    print("Available recognition engines: google (default), sphinx (offline)")
    engine_choice = input("Enter recognition engine to use: ").strip().lower() or 'google'
    transcribe_audio(file_path, engine=engine_choice)
