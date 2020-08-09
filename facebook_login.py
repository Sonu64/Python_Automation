# Importing webdriver from Selenium Web Automation Module
from selenium import webdriver
# getpass module for receiving password
from getpass import getpass

# Setting User ID, Email or Ph. No.
userId = "sonusantu64@gmail.com"

# Getting Password via getpass()
password = getpass("Enter Password: ")

# Creating browser object from ChromeDriver -> !![GIVE YOUR URL TO chromedriver.exe]!!
browser = webdriver.Chrome("C:\\Users\\NSAM\\Desktop\\IndiasSuperBrain\\chromedriver.exe")

# Providing the link to facebook to open
browser.get("https://www.facebook.com")

# Finding username element (TEXTBOX input field) in the page through its ID. For Facebook the id for username field is 'email'
userIdField = browser.find_element_by_id("email")

# Giving the element value that we have in userId
userIdField.send_keys(userId)

# Finding the element (PASSWORD input field) in the page through its ID. For Facebook the id for username field is 'pass'
passwordField = browser.find_element_by_id("pass")

# Giving the element value that we have in password
passwordField.send_keys(password)

# Finding the LogIn button through its Id - 'u_0_b'
loginButton = browser.find_element_by_id("u_0_b")

# Clicking the LogIn button
loginButton.click()

choice = input("\n\nEnter 1 to close browser: ")
while choice != "1":
    print("Invalid Choice !")
    choice = input("\n\nEnter 1 to close browser: ")
# Don't need to check for 1, as while loop ends only when 1 is given
browser.quit()
input("Press the Enter key to exit...")
    







