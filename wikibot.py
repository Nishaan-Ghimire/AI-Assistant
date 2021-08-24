import wikipedia
import basicIO as bio
def wiki():
    bio.speak("What do you Want to search sir : ")
    search = bio.voicecommand().lower()
    result = wikipedia.summary(search, sentences=2)
    bio.speak("for your search keyword the result of wikipedia is :")
    bio.speak(result)

