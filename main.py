#Import necessary packages
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import cv2
import wolframalpha
import json
import requests

#Welcome Message and speech Analyser
print('Warm Welcome by Fro')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"You asked:{statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
    speak("Warm Welcome by Fro")
    wishMe()
    if __name__=='__main__':
        while True:
            speak("Tell me how can I help you now?")
            statement = takeCommand().lower()
            if statement==0:
                continue
            if "bye" in statement or "end" in statement or "stop" in statement:
                speak('your personal assistant Fro is shutting down,Good bye')
                print('your personal assistant Fro is shutting down,Good bye')
                break
            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(f"statement", sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)
            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)
            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5) 
            elif "weather" in statement:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +str(current_temperature) +"\n humidity in percentage is " +str(current_humidiy) +"\n description " +str(weather_description))
                    print(" Temperature in kelvin unit = " +str(current_temperature) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                else:
                    speak(" City Not Found ")  
            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}") 
            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am Fro version 1 point O your persoanl assistant. I am programmed to minor tasks like''opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')       
            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by SATHYAN")    
                print("I was built by SATHYAN")
            elif "open whatsapp" in statement:
                webbrowser.open_new_tab("https://web.whatsapp.com/")
                speak("Here is whatsapp")
            elif "image" in statement or "take a photo" in statement:
                cam = cv2.VideoCapture(0)
                cv2.namedWindow("test")
                img_counter = 0
                while True:
                    ret, frame = cam.read()
                    if not ret:
                        print("failed to grab frame")
                        break
                    cv2.imshow("test", frame)
                    k = cv2.waitKey(1)
                    if k%256 == 27:
                        print("Escape hit, closing...")
                        break
                    elif k%256 == 32:
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        cv2.imwrite(img_name, frame)
                        print("{} written!".format(img_name))
                        img_counter += 1
                        cam.release()
                        cv2.destroyAllWindows()
            elif 'search' in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)       
            elif 'ask' in statement:
                speak('I can answer to computational and geographical questions and what question do you want to ask now')
                question=takeCommand()
                app_id="R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)   
            elif 'play songs' in statement or 'open music' in statement:
                music_dir = 'H:\AUDIOS\songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
                time.sleep(3)  
            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
                time.sleep(3)    
