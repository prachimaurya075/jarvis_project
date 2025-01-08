import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

r = sr.Recognizer()
engine = pyttsx3.init()
# global library


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open gooogle " in c.lower():
        webbrowser.open("https://google.com")
        
    elif "open Youtube " in c.lower():
        webbrowser.open("https://Youtube.com")
        
    elif "open facebook " in c.lower():
        webbrowser.open("https://facebook.com")
        
    elif "open Linkedin " in c.lower():
        webbrowser.open("https://Linkedin.com")
        
    elif "open instagram " in c.lower():
        webbrowser.open("https://instagram.com")  
        
    elif "open Twitter " in c.lower():
        webbrowser.open("https://Twitter.com")   
    elif c.lower().startswith("Play"):
        song= c.lower().split(" ")[1]
        link = music_library.music[song] 
        webbrowser.open(link)
        
    
        
        
          
        
                    


    if __name__ == "__main__":
         speak("Initializing Jarvis.....")
    
    while True:
        try:
            # Obtain audio from the microphone
            with sr.Microphone() as source:
                
                print("Listening.........")
               
                audio = r.listen(source, timeout=5, phrase_time_limit=1)

            # Recognize speech using Google Speech Recognition
            word = r.recognize_google(audio)
            if(word.lower()=='jarvis'):
                speak("Ya")
           
#Listen for the command
            
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

               
                
                    processCommand(command)
        
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
