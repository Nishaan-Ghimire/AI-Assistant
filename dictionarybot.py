
import basicIO as bio
from PyDictionary import PyDictionary
dictionary=PyDictionary()
def search_meaning():
    bio.speak("What word do you want to search sir")    
    smeaning = bio.voicecommand().lower()
    print(smeaning)
    omeaning = dictionary.meaning(smeaning) # Getting the meaning
    words = list(omeaning.keys()) # Getting list of keys which has meaning like noun verb etc
    bio.speak(f"The word {smeaning} can be used as")
    for x in words: # Looping to print them all
        bio.speak(x)
    for x in words: # Looping to print meaning of all
        meaning = omeaning[x][0]
        bio.speak(f"as {x} the meaning of {smeaning} is {meaning}")
        search_meaning()
        bio.speak("Thank you for asking me :)")




