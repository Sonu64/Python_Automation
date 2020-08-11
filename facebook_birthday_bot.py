# Generally each comment is a description of the line below it,but when this rule is broken you will get it and will have no problems in understanding 

from selenium import webdriver
from getpass import getpass
#common keys required because we have to press the Enter key after wishing
from selenium.webdriver.common.keys import Keys

# BOTTOM PROCESS IS FOR LOGIN TO FACEBOOK, SEE THE facebook_login.py FOR COMMENTS #
userId = "YOUR USERNAME HERE"
password = "YOUR PASSWORD HERE"
browser = webdriver.Chrome("C:\\Users\\NSAM\\Desktop\\IndiasSuperBrain\\chromedriver.exe")
browser.get("https://www.facebook.com")
userIdField = browser.find_element_by_id("email")
userIdField.send_keys(userId)
passwordField = browser.find_element_by_id("pass")
passwordField.send_keys(password)
loginButton = browser.find_element_by_id("u_0_b")
loginButton.click()
# UPTO HERE #

# Under notifications section of the classic version of FB, current birthdays are all under an  ANCHOR tag with class of "fbReminderStory". The bottom code returns a string something like - """birthdayJohn Doe and 4 others"""
note = browser.find_element_by_class_name("fbRemindersStory")
# Reverse the text, and get the number of people those have birthdays, +1 bcoz Fb says John Doe and 'n' others 
num = int(note.get_attribute('textContent')[::-1][7])+1
# Then go to the birthdays page
browser.get("https://www.facebook.com/events/birthdays/")
# All the wish giving text areas are under the class "enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput". We are getting all those text areas through XPATH. Note that it is 'find_elements' and not 'find_element' !!
bDayList = browser.find_elements_by_xpath("//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
# For loop will run through all the textareas, but it should wish only the first 'num' people, so we use a seperate variable 'c' to check for first 'num' runs of the for loop. The for loop iterates over each textarea bDayList....Look above !
c = 0
for element in bDayList:
    # element is current textarea - all same class, but ID is different that we are getting in the below line
    elementId = str(element.get_attribute('id'))
    # all the textAreas have different Ids, we are getting it in the above line as it will help us send_keys to that textArea. Now in the below line we are dynamically creating a seperate XPATH for each textArea
    XPATH = '//*[@id = "' + elementId + '"]'
    # finding the textArea to write message
    wish = browser.find_element_by_xpath(XPATH)
    # writing message
    wish.send_keys("Happy Birthday from Sonu's Birthday Bot !")
    # Pressing the ENTER key, ----- Keys.RETURN will also work
    wish.send_keys(Keys.ENTER)
    # increae c by 1, 1 person wished !
    c += 1
    # if first 'num' persons are wished, break the for loop
    if c >= num:
        break
    
# very basic exit system
choice = input("\n\nEnter 1 to close browser: ")
while choice != "1":
    print("Invalid Choice !")
    choice = input("\n\nEnter 1 to close browser: ")
# Don't need to check for 1, as while loop ends only when 1 is given
browser.quit()
input("Press the Enter key to exit...")






