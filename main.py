# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import music_library
# import requests

# r = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "099fa52203c84001ae7f95a39d856c7e"  # Your News API Key


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
        
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
        
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
        
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
        
#     elif "open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")  
        
#     elif "open twitter" in c.lower():
#         webbrowser.open("https://twitter.com")
        
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ", 1)[1]  # Fetch the song name after 'play'
#         link = music_library.music.get(song, None)
#         if link:
#             webbrowser.open(link)
#         else:
#             speak(f"Sorry, I couldn't find the song {song}.")
            
#     elif "news" in c.lower():
#         try:
#             url = "https://newsapi.org/v2/everything"
#             params = {
#                 'q': 'tesla',
#                 'from': '2024-08-18',
#                 'sortBy': 'publishedAt',
#                 'apiKey': newsapi
#             }

#             r = requests.get(url, params=params)

#             if r.status_code == 200:
#                 data = r.json()
                
#                 # Create an empty list to store the titles
#                 titles = [article['title'] for article in data['articles']]
                
#                 # Speak out the first few headlines
#                 for title in titles[:5]:  # Limit to 5 headlines
#                     speak(f"Here is a headline: {title}")
#             else:
#                 speak(f"Error fetching news: {r.status_code}")
#         except Exception as e:
#             speak(f"An error occurred: {e}")
            
            
#         else:  
#             #let opeNAI handle that request
#             pass    


# if __name__ == "__main__":
#     speak("Initializing jarvis.....")
    
#     while True:
#         try:
#             # Obtain audio from the microphone
#             with sr.Microphone() as source:
#                 print("Listening.........")
#                 audio = r.listen(source, timeout=5, phrase_time_limit=5)

#             # Recognize speech using Google Speech Recognition
#             word = r.recognize_google(audio)
#             if word.lower() == 'jarvis':
#                 speak("Yes, how can I assist you?")
           
#                 # Listen for the command
#                 with sr.Microphone() as source:
#                     print("Jarvis Active....")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)
#                     processCommand(command)
        
#         except sr.UnknownValueError:
#             # Uncomment this if you want it to speak when speech isn't recognized
#             # speak("Sorry, I didn't catch that.")
#             pass
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")
#         except Exception as e:
#             print(f"Error: {e}")


import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Replace with your News API Key
newsapi = "099fa52203c84001ae7f95a39d856c7e"

# Music Library: Map song names to YouTube URLs
music_library = {
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
}

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to play songs
def play_song(song_name):
    song_name = song_name.lower()
    if song_name in music_library:
        song_url = music_library[song_name]
        if song_url.startswith("http"):  # If it's a URL
            webbrowser.open(song_url)
            speak(f"Playing {song_name} on YouTube.")
        else:  # If it's a local file
            mixer.music.load(song_url)
            mixer.music.play()
            speak(f"Playing {song_name}.")
    else:
        speak(f"Sorry, I couldn't find the song {song_name}.")

# Process commands
def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "open twitter" in c:
        webbrowser.open("https://twitter.com")
    elif c.startswith("play"):
        song = c.split(" ", 1)[1]
        play_song(song)
    elif "news" in c:
        try:
            url = "https://newsapi.org/v2/top-headlines"
            params = {
                'q': 'latest',
                'language': 'en',
                'apiKey': newsapi
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                articles = response.json().get('articles', [])
                for article in articles[:5]:
                    speak(f"Headline: {article['title']}")
            else:
                speak(f"Error fetching news: {response.status_code}")
        except Exception as e:
            speak(f"An error occurred while fetching news: {e}")
    else:
        speak("I am sorry, I can't perform that action.")

if __name__ == "__main__":
    speak("Jarvis is now online.")
    print("Jarvis is ready to assist you.")
    
    with sr.Microphone() as source:
        # Reduce ambient noise for better accuracy
        r.adjust_for_ambient_noise(source, duration=0.5)
        
        while True:
            try:
                print("Listening for 'Jarvis'...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)

                # Recognize activation keyword
                word = r.recognize_google(audio)
                if word.lower() == 'jarvis':
                    speak("Yes, how can I assist you?")
                    print("Listening for your command...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processCommand(command)

            except sr.UnknownValueError:
                # No speech detected or not understood
                print("I didn't catch that. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
