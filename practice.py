from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
w = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
w.get("https://www.youtube.com")















# import basicIO as bio 
# from  playsound import playsound
# # playsound('D:\\Mp3 player\\songs\\Alan Walker - Alone (Lyrics).mp3')

# def check():
#     text = bio.voicecommand().lower()
#     bio.speak(text)
#     if text == "can you listen" or "jara" or "zara":
#          bio.speak("Yeah I can hear try by increasing distance")
#     else:
#          bio.speak("Sorry I cannot hear. please try again")
#     check()    
# check()
