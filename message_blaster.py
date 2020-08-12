from selenium import webdriver
browser = webdriver.Chrome("C:\\Users\\NSAM\\Desktop\\IndiasSuperBrain\\chromedriver.exe")
browser.get("https://www.amazon.in/ap/forgotpassword?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&ignoreAuthState=1&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&prevRID=D7NPT2BJ2AKQ9QCJNHP8&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&prepopulatedLoginId=eyJjaXBoZXIiOiIxbGk2cGd6VFJwMncwcTMrVFh4ZmNBPT0iLCJ2ZXJzaW9uIjoxLCJJViI6IlNyK2FSL1ZhM1lidVRMRTd3a0doRmc9PSJ9&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&timestamp=1597250596000")

phoneNumberBox = browser.find_element_by_id("ap_email")
phoneNumberBox.clear()
phoneNumberBox.send_keys("+917047810778")
button = browser.find_element_by_id("continue")
button.click()
for i in range(20):
    resendOTPbutton = browser.find_elements_by_tag_name("a")[1]       
    resendOTPbutton.click()
browser.quit()



