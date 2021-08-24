from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import basicIO as bio
playlist = input("Which playlist do you want to play sir you have :\n Playlist 1 \n Playlist 2").lower()
browser = webdriver.Chrome(executable_path=r'chromedriver.exe')

if(playlist ==  "1" or playlist == "playlist 1" or playlist == "no 1" or  playlist == "first" or playlist == "first one"):
    browser.get('https://open.spotify.com/playlist/52IFCGqubyZKjK1OhtWQZ6')
    time.sleep(10)
    play = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]')
    time.sleep(3)
    close = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div[2]/button')
    time.sleep(3)
    play = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]')
    play.click()
elif(playlist ==  "2" or playlist == "playlist 2" or playlist == "no 2" or playlist == "second" or playlist == "second one"):
    browser.get('https://open.spotify.com/playlist/6GuErkiVhO9i0viUX89P3u')
    time.sleep(10)
    play = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]')
    time.sleep(3)
    close = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div[2]/button')
    time.sleep(3)
    play = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]')
    play.click()



