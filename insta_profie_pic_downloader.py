from selenium import webdriver
#common keys required because we have to press the Enter key after wishing
from selenium.webdriver.common.keys import Keys
import urllib.request
userHandle = input("Enter user handle to download Profile Pic: ")
url = "https://www.instagram.com/" + userHandle
browser = webdriver.Chrome("C:\\Users\\NSAM\\Desktop\\IndiasSuperBrain\\chromedriver.exe")
browser.get(url)
try:
    pic = browser.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
    pic = browser.find_element_by_xpath('//img[@class="be6sR"]')

picLink = pic.get_attribute("src")
urllib.request.urlretrieve(picLink, "C:\\Users\\NSAM\\Desktop\\IndiasSuperBrain\\"+userHandle+".jpg")
print("Successfully downloaded the Profile Picture of " + userHandle + " in C:\\Users\\NSAM\\Desktop\\IndiasSuperBrain")