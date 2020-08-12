from selenium import webdriver
from getpass import getpass
#common keys required because we have to press the Enter key after wishing
from selenium.webdriver.common.keys import Keys
import time

def blast():
    userId = "Your Username here"
    password = "Your password here"
    browser = webdriver.Chrome("C:\\Users\\NSAM\\Desktop\\IndiasSuperBrain\\chromedriver.exe")
    
    # The complete post URL directly with Login, at first directly go to the story without signing in to FB, from there click on Login button, then your get a URl something like below
    postURL = "https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fstory.php%3Fstory_fbid%3D183397699825094%26id%3D100044645959888&ref=104&rs=26&rid=100044645959888&refsrc=https%3A%2F%2Fm.facebook.com%2Fstory.php&refid=52"
    browser.get(postURL)
    userIdField = browser.find_element_by_id("m_login_email")
    userIdField.send_keys(userId)
    passwordField = browser.find_element_by_id("m_login_password")
    passwordField.send_keys(password)
    loginButton = browser.find_element_by_link_text("_54k8._52jh._56bs._56b_._28lf._9cow._56bw._56bu")
    # OR browser.find_element_by_link_text("Resend OTP")
    loginButton.click()
    time.sleep(10)
    for i in range(1000):
        time.sleep(3)
        commentBox = browser.find_element_by_id("composerInput")
        commentBox.send_keys("Bot Comment")
        time.sleep(1)
        sendButton = browser.find_elements_by_tag_name("button")[0]
        sendButton.click()
        
blast()

