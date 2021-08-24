import basicIO as bio
import youtubebot as ubot
import googlebot as googlebot
import instabot as instabot
import wikibot as wikibot
import dictionarybot as dbot
import basicIO as bio
# import spotify as spot
import datetime

# function for wishing  
def wishme():

    wishtime = int(datetime.datetime.now().hour)
    print(wishtime)
    if wishtime <= 0 and wishtime > 12:
       bio.speak("Good Morning Sir")
    elif wishtime <= 12 and wishtime > 17:
       bio.speak("Good Afternoon sir")
    elif wishtime <= 17 and wishtime > 20:
       bio.speak("Good Evening Sir") 
    elif wishtime <= 20 and wishtime > 24:
       bio.speak("Hi Sir, Haven't you slept Yet ?")   
    else:
       bio.speak("Hi sir,")        
    # bio.speak('What can I do for you ?')


def task():
    work = bio.voicecommand().lower()

    #for youtube
    if(work == "search youtube" or work == "open youtube"):
        ubot.searchtube()
    #for google
    elif(work == "search google" or work == "search something" or work == "open google"): 
        googlebot.googleit()    
    # for exiting repeat command
    elif(work == 'no' or work == 'not at all' or work == 'no thank you'):
        bio.speak("anyway thank you for remembering me ") 
      #for instagram  
    elif(work == "check my insta" or work == "check my instagram" or work == "open instagram" or work == 'open my instagram' or work == 'open my insta'):
        instabot.checkinsta()
      #for wikipedia
    elif(work == "search meaning" or work == "search defination" or work == "open wikipedia"):
        wikibot.wiki()
      #for music
    elif(work == "play music" or work == "play song" or work == "play songs" or work == "gaana lagado"):
        bio.speak("What would prefer youtube or spotify sir")
        choose = bio.voicecommand().lower()
        if(choose == "youtube" or choose == "play from youtube" or choose == "use youtube"):
            ubot.playtubesong()    
        elif(choose == "spotify" or choose == "play from spotify" or choose == "use spotify"):
            spot.playsongs()
        # elif(choose == "quit"):
        #     break    
        else: 
            bio.speak("sorry sir would you repeat once again or say quit to quit program") 
            task()   
    elif(work == 'search meaning' or work == 'search word'):
        dbot.search_meaning()
    else:
        bio.speak("Sorry sir I am unable to understand you I am in Development Phase") 
        # bio.speak("anyway thank you for remembering me ")    
    bio.speak('is there anything more sir')
    task()
          

wishme()
task()
    