from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import basicIO as bio

def googleit():
    bio.speak("what do you want to search sir: ")
    search = bio.voicecommand().lower()
    print("okay sir Please wait :) ")
    browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
    browser.get("http://www.google.com")
    write = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    write.send_keys(search)
    write.send_keys(Keys.ENTER)
    time.sleep(6)
    bio.speak("Here is your result sir !!")

