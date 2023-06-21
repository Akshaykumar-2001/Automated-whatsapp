from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
PATH = "path_to_chromedriver"

# Initialize the Chrome WebDriver with a Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com/")
driver.maximize_window()


text= "Hello ! Dear  "
text2=", Akshay is sleeping right now!.This is an auto generated reply from his bot. Thanks! Have a nice day :)"


time.sleep(30) # 30 sec. to scan the QR code 

namelist = ["Akka","Amma","Sri"] # List of names 

while(True):
    for name in namelist:

        search_box = driver.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p') # search-bar 
        search_box.click()
        time.sleep(3)


        unread_button = driver.find_element('xpath','//*[@id="side"]/div[1]/div/button/div/span') #un-read filter
        unread_button.click()

        # Type the name of contact
        search_box.send_keys(name)
        time.sleep(3)
        
        # Check if there is any unread message
        unreadMsgs=False

        get_list=driver.find_elements('xpath',"//span[@class ='matched-text _11JPr']")#matched **
        if(len(get_list)):
            unreadMsgs=True
 
        if unreadMsgs:
            #Chat
            user=driver.find_element('xpath','//span[@title = "{}"]'.format(name))
            user.click()

            # Type  message on Chatbox
            textbox=driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            textbox.send_keys(text)
            textbox.send_keys(name)
            textbox.send_keys(text2)

            # Send Message
            send=driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            send.click()

            
            print(name,"texted you!") # Print name in terminal

            time.sleep(5)
    
        unread_button = driver.find_element('xpath','//*[@id="side"]/div[1]/div/button/div/span') # unrread button
        unread_button.click()

        back_to=driver.find_element('xpath',"//*[@id='side']/div[1]/div/div/button/div[2]/span")
        back_to.click()
    time.sleep(200) #again run after 200 sec.
driver.quit()
