from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import basicIO as bio

def searchtube():
    browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
    bio.speak("what do you want to search sir : ")
    search = bio.voicecommand()
    # timePeriod = input("how long do you want to listen Please provide in min : ")
    openbrowser()
    browser.get("https://www.youtube.com/results?search_query="+search)
    print("okay sir")
    time.sleep(6)
    play = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img')
    play.click()
    time.sleep(10*60)

def playtubesong():
     bio.speak("sir, I am playing song from your youtube playlist : ")
     bio.speak("how much time do you want to set sir ?")
     time_interval = bio.voicecommand().lower()
     openbrowser()
     browser.get("html")
     time.sleep(int(time_interval) * 60)
     

