import time
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
 
import requests
 
# variable to store the name of the contact
contact = "Test"
#variable to store message
message = "Hi, this is an automated message"

url = "https://web.whatsapp.com"

#open a Whatsapp Web interface which automatically asks you to scan the QR code
driver = webdriver.Chrome()
driver.get(url)
print("Scan QR Code and press Enter")
input() # used to pause the interface until user presser enter
print("Running ...")


#finding search bar
def find_contact(contact):
    inp_xpath_search = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    input_box_search = WebDriverWait(driver, 50).until(
        lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search.click() #clicks on search bar
    time.sleep(0)
    input_box_search.send_keys(contact) #enters name of contact
    time.sleep(0.2)

    #finds contact
    selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
    selected_contact.click() # select contact

#find message box
def send_message(message):
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(0.2)
    input_box.send_keys(message + Keys.ENTER) #enters message
    time.sleep(0)


find_contact(contact)

#prints the automated message multiple times
for count in range (20):
    send_message(f'{message} {count+1}/20')

