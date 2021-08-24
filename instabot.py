from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import basicIO as bio


browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
def logininsta():
    bio.speak('sir please type the password for security purpose')
    psw = input()
    bio.speak('thank you sir , please wait ...')
    browser.get("https://www.instagram.com")
    time.sleep(10)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")
    username.send_keys("__nishann__")
    password.send_keys(psw)
    login.click()
    time.sleep(8)
    not_now = browser.find_element_by_css_selector("[class = 'sqdOP yWX7d    y3zKF     ']")
    not_now.click()
    time.sleep(8)
    offit = browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
    offit.click()
    # browser.execute_script("window.scrollTo(0,1000);")
    # time.sleep(1)
    # browser.execute_script("window.scrollTo(0,3000);")
    time.sleep(2)
def checkinsta():
    logininsta()
    for x in range(1,100):
        header_name = len(browser.find_elements_by_css_selector('#react-root > section > main > section > div > div:nth-child(2) > div > article:nth-child('+str(x)+') > header > div.o-MQd > div:nth-child(1) > div > span > a'))
        print(header_name)
        time.sleep(2)
        like = browser.find_elements_by_css_selector("[class='ZyFrc']")[x]
        actionChains = ActionChains(browser)
        actionChains.double_click(like).perform() 
   
def followreq():
    logininsta()
    bio.speak('Sir could you spell the username please ')
    fri_usr_name = bio.voicecommand().lower()
    search_btn = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search_btn.send_keys(fri_usr_name.strip())
    search_btn.send_keys(Keys.ENTER)
logininsta()

