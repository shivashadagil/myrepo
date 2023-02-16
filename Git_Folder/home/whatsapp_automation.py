from django.shortcuts import render, redirect
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from .conf import CHROME_PROFILE_PATH

from .models import *


def send_message(message, contacts, files):
    try:
        # contacts = ['Wife'] #,'99807 11954','97425 82345','97425 83456','97425 84567','97425 85678','93425 24127','93435 #24127','99015 24127','99025 24127','97435 24127','99864 15541']#'9964624127','9742524127',
        
        contacts = contacts
        msg = message
        files = files

        Options = webdriver.ChromeOptions()
        Options.add_argument(CHROME_PROFILE_PATH)
        #browser = webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe", options=Options)
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=Options)
        browser.maximize_window()
        browser.get('https://web.whatsapp.com/')


        #for i in range(2):   
        for contact in contacts:
            try:
                search_xpath = '//div[@data-tab="3"][@data-testid="chat-list-search"]'
                search_box = WebDriverWait(browser, 50000).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
                search_box.clear()
                time.sleep(1)
                pyperclip.copy(contact)       
                search_box.send_keys(Keys.CONTROL + "v")
                time.sleep(1)
                contact_xpath = '//div[@class="_8nE1Y"]'
                #contact_title = browser.find_element(By.XPATH, contact_xpath)
                contact_title = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,contact_xpath)))
                # print('*********************************',contact_title.value())
                time.sleep(10)
                contact_title.click()
                time.sleep(10)
    
                file = add_files.objects.all()

                if file != None:
                    
                    for image in range(file.count()):

                        attachement_box = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'//div[@title="Attach"]')))
                        # print('*********************************',contact_title.value())
                        attachement_box.click()
                        time.sleep(1)

                        # image_ = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH,'//span[@data-icon="attach-image"]')))
                        # # print('*********************************',contact_title.value())
                        # image_.click()
                        link="C:\\Users\\SHREEG\\Desktop\\whatsapp_automation\\media\\user_files\\"+ str(image+1) +".jpeg"
                        # pyperclip.copy(msg)  
                        # input_box.send_keys(Keys.CONTROL + "v")
                        # time.sleep(2)
                        # input_box.send_keys(Keys.ENTER)
                        # #input_box.click()
                        
                    

                        image_box = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
                        # print('*********************************',contact_title.value())
                        image_box.send_keys(link)
                        time.sleep(1)

                        send_btn = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'//span[@data-icon="send"]')))
                        send_btn.click()
                        time.sleep(1)


                input_xpath = '//div[@data-tab="10"][@data-testid="conversation-compose-box-input"]'
                #input_box = browser.find_element(By.XPATH, input_xpath)
                input_box = WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
                time.sleep(2)
                pyperclip.copy(msg)  
                input_box.send_keys(Keys.CONTROL + "v")
                time.sleep(3)
                input_box.send_keys(Keys.ENTER)
                #input_box.click()
                time.sleep(2)   
            except:
                pass
        browser.close()
        time.sleep(1)
        return 
    except:
        return redirect('/')