import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 130
engine.setProperty('rate',newVoiceRate)


# function for speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function for taking voice command
def voicecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold = 100
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-IN')    
        print(f'I listened : {query}\n')

    except Exception as e:
        print('Sorry I cannot hear could you say that again !')
        voicecommand()
        return "none"
    return query 


