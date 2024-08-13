import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello Sir, I am robo version 1.0, build by anuj. How can I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        try:
            audio = r.listen(source)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return "None"
        except sr.RequestError:
            print("Request failed; perhaps no internet connection?")
            return "None"
        except Exception as e:
            print(f"Error during listening: {e}")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"
    except Exception as e:
        print(f"Recognition error: {e}")
        return "None"

    return query


def get_wikipedia_summary(query, sentences=2):
    """Fetch a summary from Wikipedia using wikipedia package."""
    wikipedia.set_lang("en")
    wikipedia.summary(query, sentences=sentences)
    summary = wikipedia.summary(query, sentences=sentences)
    return summary

if __name__ == "__main__":
    wish_me()
    if 1:
    #while True
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            try:
                results = get_wikipedia_summary(query)
                if results:
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                else:
                    speak("Sorry, I couldn't find any information on that topic.")
            except Exception as e:
                speak("Sorry, there was an error in retrieving the information.")
                print(f"Error: {e}")

        elif 'open youtube' in query:
            speak("sure sir Open YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("sure sir Open Google")
            webbrowser.open("https://www.google.com")
        elif 'open chat gpt' in query:
            speak("sure sir Open Chat gpt")
            webbrowser.open("https://chatgpt.com")
        elif 'open docker hub' in query:
            speak("sure sir Open docker hub")
            webbrowser.open("https://hub.docker.com")
        elif 'open github' in query:
            speak("sure sir Open github")
            webbrowser.open("https://github.com/")
        elif 'play music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Sure sir playing music")
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\kkart\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Sure sir Openning vs code")
            os.startfile(codePath)

        elif 'open docker desktop' in query:
            Path = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
            speak("Sure sir Openning docker desktop")
            os.startfile(Path)

        elif 'open photos' in query:
            img_dir = 'C:\\photos'
            photos = os.listdir(img_dir)
            speak("Sure sir Openning photos")
            os.startfile(os.path.join(img_dir, photos[0]))



