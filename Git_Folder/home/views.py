
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
from .whatsapp_automation import *
from .models import *
import pathlib
import os




# Create your views here.

# def contacts(request):
#     # print('****************************1*****************************')
#     # chrome_options = Options()
#     # print('****************************2*****************************')
#     # chrome_options.add_argument("--user-data-dir=chrome-data")
#     # print('****************************3*****************************')
#     # driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
#     # #driver = webdriver.Chrome('C:\\chromedriver\\chromedriver')
#     # print('****************************4*****************************')
#     # driver.get('https://web.whatsapp.com/')
#     # print('****************************5*****************************')

#     # browser = webdriver.Chrome('C:\\ChromeDriver\\chromedriver.exe')
#     # browser.maximize_window()
#     # browser.get('https://web.whatsapp.com/')


#     # time.sleep(15)
#     # print('****************************6*****************************')

#     # #contact_group = WebDriverWait(browser,500).until(browser.find_elements(By.XPATH,'//div[@class="_21S-L"]'))

#     # contact_group = browser.find_elements(By.XPATH,'//div[@class="_21S-L"]')

#     # print(len(contact_group),'****************************7*****************************')

#     # #search_xpath = '//div[@class="_21S-L"]'

#     # time.sleep(20)
#     # browser.close()

#     # #contact_group = WebDriverWait(browser, 500).until(EC.element_to_be_selected((By.XPATH, search_xpath)))
    
    

#     # # print('****************************7*****************************')

#     # contact_list = []
#     # print('****************************8*****************************')

#     # # for i in contact_group:
#     # #     time.sleep(0.2)
#     # #     contact = contact_group.find_element(By.XPATH,'.//span[@dir="auto"]').text
#     # #     contact_list.append(contact)
#     # #     print(i,'************************') 

#     # # print(contact_list)

#     # return render(request, 'home.html',locals())   

#     driver = webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe")
#     wait = WebDriverWait(driver, 150)
#     actions = ActionChains(driver)
#     driver.get('https://web.whatsapp.com/')

#     wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='g0rxno12' and @class='_21S-L']")))

#     #WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_3Dr46']")))
#     time.sleep(3)
#     all_names =wait.until(lambda driver:driver.find_elements(By.XPATH,"//div[@class='g0rxno12' and @class='_21S-L']"))

#     print(len(all_names),'********************************************')
    
#     for i in all_names:
#         time.sleep(1)
#         actions.move_to_element(i).perform()
#         print(i.text)
#     driver.close()
#     return render(request, 'home.html',locals())

def home(request):
    message = "Welcome to What's App automation."
    contacts = contact_list.objects.all()
    return render(request, 'home.html', locals())

    
def whatsapp_automation(request):
    if request.method == 'POST':
   
        message = request.POST['message']  
        contacts = None
        files = None

        user_contacts = request.POST['text_area_contacts']

        if len(user_contacts) > 0:
            contacts = user_contacts.split('\r\n')
        else:
            return redirect('/')
            
        send_message(message, contacts, files)
        time.sleep(1)

        return redirect('/')

def add_contact(request):
    if request.method == 'POST':

        add_contact = contact_list()
        add_contact.contact_name = request.POST['contact']
        add_contact.category = request.POST['category']
        add_contact.save()

        message = "Contact added successfully"
        return render(request, 'home.html', {'message':message})
    return render(request, 'home.html', {'message':"Somethink went wrong please try again."})
    

def add_user_files(request):
    if request.method == 'POST':
        count = add_files.objects.all().count()
        filename = count+1

        add_file = add_files()
        # add_file.file_name = request.FILES['doc']


             
        add_file.file_name = request.FILES['doc']
        file_extension = pathlib.Path(str(request.FILES['doc'])).suffix
        add_file.file_name.name = str(filename) + file_extension
        add_file.save()
      
        message = "File added successfully."
        return redirect('/')

def delete_images(request):
    ids = add_files.objects.values_list('id')
   

    for i in ids:

        list[i]
        prod = add_files.objects.get(id=i[0])
        
        if len(prod.file_name) > 0:
            os.remove(prod.file_name.path)
        prod.delete()
            # messages.success(request,"Product Deleted Successfuly")
    return redirect('/')










    #     print(i,'********************************')

    #     img = add_files.objects.get(img_number = i+1)
    #     img.delete()
    # return redirect('/')


    



def view_contacts(request):
    contact = contact_list.objects.all()
    return render(request, 'contact.html',{'contacts':contact})


        
        

    # time.sleep(2)
    # search_input = browser.find_element(By.NAME, "q")
    # search_input.send_keys('Hello world')

    # time.sleep(2)

    # search_input = browser.find_element(By.NAME, "btnK")
    # search_input.click()

   
"""
<input id="input" type="search" autocomplete="off" spellcheck="false" role="combobox" placeholder="Search Google or type a URL" aria-live="polite">

//*[@id="inputWrapper"]

//*[@id="input"]

<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" role="button" tabindex="0" type="submit" data-ved="0ahUKEwi5sNXPuqj8AhXaSWwGHfvbAPMQ4dUDCA4">


<div data-testid="chat-list-search" title="Search input textbox" role="textbox" class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="3" dir="ltr"></div>


<p class="selectable-text copyable-text"><br></p>

<div class="fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv" contenteditable="true" role="textbox" spellcheck="true" title="Type a message" data-testid="conversation-compose-box-input" data-tab="10" data-lexical-editor="true" style="user-select: text; white-space: pre-wrap; word-break: break-word;"><p class="selectable-text copyable-text"><br></p></div>


<div class="_21S-L"><span dir="auto" title="Wife" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr">Wife</span></div>

<div class="_21S-L"><span dir="auto" title="Gurubai Akka" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr">Gurubai Akka</span></div>



"""

"""[9964031447,9036284373,9743234084,9845608993,9945906635,7795556283,9986748851,9663227222,9342134826,9008249606,7899944486,7760603041,9448582995,9343031613,9902393223,8660905223,9482889711,9901308281]

        8971594050,9886819351,9947150024,9742577500,9847151664,9332193598,9740842520,9887347795,9980487395,9019040759,9948453428,9988435125,9886743578,8899144566,9887147096,7676666476,9999147975,9988149097,9966149786,9947735696,9980398720,8070609111,8867293855,8147244493,7353136826,9880055328,9844905529,9972163687,9900608161,9742319777,9535230879,8223755536,9060566666,6320958815,8247798684,9884140678,8618567963]
        9886676116,9342998522,9964205723,9480322812,9019209225,8123143136,7890475572,8050957321,9036668885,9945442594,9884478338,9739349777,9538441339,9241374425,9986267623,9741881395,8904262728,8867816131,7676857575,9379329626,9964763394,9742045786,9595962987,8884118839,9743299458,]
        9448505342,9343296327,9880012635,9343808007,9353539022,8123023099,9945281488,8482225363,8951512666,9739638298,8884442987,9880566270,9449644323,9019848143,9880109690,7353666638,9342208595,8971594050,9741088437,9739414048,8970501051,9945283494,9945283494,9449048321,9343372999]
        9964031447,9036284373,9743234084,9845608993,9945906635,7795556283,9986748851,9663227222,9342134826,9008249606,7899944486,7760603041,9448582995,9343031613,9902393223,8660905223,9482889711,9901308281,9880681010,9620932025,8310814394,8008534804,7795030655,9916150201,9900741999,9535094696,7411211885,9113225468,9380739213,9666322020,9036513263,8186003342,7975744795,9916686163,9008879151,9513069222,8880887562,9535817898,7676102025,8884235430,9448877275,9591112310,8971152604,9986114136,9449336937,9113939471,9880736386,8867301143,7022772083,9964652253,9343554565,7353338089,9986936551,9663117248,9448605307,7899603894,9731308017,8073860016,9448975209,9481294774,9242411485,7019937614,9448444038,8722134121,7411109200,7899650851,9148982434,9880235154,9901225698,6360954480,7019789892,9738417190,9071411168,9902584364,9341111136,9739126817,8861425077,9845610111,8951527969,9701821456,9738127247,9008387050,8310373190,8105864703,9342890193,7676003050,8971803030,8088420052,9916991781,7829480346,7676770930,9900832942,9880292935,9845010871,8722046660,9448335975,9036540513,9945080606,9343438482,9886779242,9448587735,8792446047,8861857636,9110633079,8951100182,6361255739,8904019564,9731788095,7892790974,7619617518,9035809285,8494942222,9611673894,9986547543,6360147350,9880080807,6305158391,9986850544,9902561911,9535014058,9448038851,8310488062,9945747360,9980444818,8951819171,9448125859,7353938321,9036558894,8150934567,9448222592,9448579817,9900248100,9448572115,9742974125,9448897791,9731549953,9731549953,7353211948,7829568283,7204166487,7019914574,8880527545,8123532387,8790919995,9900226615,8073442712,9845383685,9900741767,7038583926,9164602995,9739363416,9035304421,8618594040,9886513658,9035304421,6366190991,9845383685,9611445353,9740409873,9164006434,6305158391,9448403068,9110264681,"""
