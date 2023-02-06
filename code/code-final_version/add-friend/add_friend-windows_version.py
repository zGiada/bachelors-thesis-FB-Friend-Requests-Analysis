import json
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import datetime

def check_cod_id(cod_id):
    with open("../dataset/profili-fake.json", "r") as f:
        readJSONfile = json.load(f)
        not_found = True
        temp = readJSONfile["male"]
        for i in temp:
            if (i["cod_id"] == int(cod_id)):
                email = i["email"]
                password = i["pwd"]
                not_found = False
        if not_found:
            temp = readJSONfile["female"]
            for i in temp:
                if (i["cod_id"] == int(cod_id)):
                    email = i["email"]
                    password = i["pwd"]
                    not_found = False
    if not_found:
        return "false"
    else:
        return email, password

def delete_cache():
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0])

def choose_url(type):
    time.sleep(3)
    with open("../victims.json", "r") as f:
        readJSONfile = json.load(f)
        temp = readJSONfile[type]
        l = int(len(temp)) - 1
        value = randint(0, l)
        url = temp[value]["url"]
    f.close()
    if (len(temp) == 0):
        return "false"
    else:
        return url

def add(attack, url, type_profile):

    #go to the profile page to add
    try:
        driver.get(url)
        time.sleep(5)
        #send friend request
        try:
            try:
                driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz bp9cbjyn j83agx80 pfnyh3mw j5wkysh0 hytbnt81']").click()
            except:
                try:
                    driver.find_element_by_xpath("//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l cbu4d94t taijpn5t k4urcfbm']").click()
                except Exception as e:
                    print(e)
            #class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l cbu4d94t taijpn5t k4urcfbm"

            time.sleep(5)
            print("friend request sent")
            time.sleep(5)

            today = datetime.date.today()
            #insert request on request-log
            item_data = {}
            with open("request-log.json", "r+") as f:
                readJSONfile = json.load(f)
                temp = readJSONfile[attack]
                item_data["victim"] = url
                item_data["date"] = str(today)
                item_data["type"] = type_profile
                temp.append(item_data)
            with open("request-log.json", "w") as c:
                json.dump(readJSONfile, c, indent=4)
            print("save request")

        except Exception as e:
            print("friend request not sent")
            print(e)
    except Exception as e:
        print(e)
        print("Wrong email and/or password and or link")



# ------------- MAIN ------------- #

if len(sys.argv) != 2:
    print("incorrect number of parameters entered")
    sys.exit()

nome_script, round = sys.argv

tit = [ 1, 1, 2, 3, 3, 2, 3, 3, 3, 3, 2, 
        4, 2, 2, 1, 3, 3, 3, 2, 3, 2, 2, 
        2, 3, 2, 3, 1, 5, 2, 3, 3, 3, 1,
        4, 1, 3, 2, 3, 1, 2, 3, 1, 3, 1,
        3, 1]
counting = tit[int(round)]
first_element = 0
r=0
while r < int(round):
    first_element = first_element + tit[r]
    r=r+1

type_vic = []
with open("../victims.json", "r+") as f:
    readJSONfile = json.load(f)
    for m in readJSONfile:
        name = str(m)
        type_vic.append(name)
f.close()
list_type_vic = sorted(type_vic)

'''
list_attacker = [
#    'PF-0', 
#    'PF-1', 
    'PF-10', 
    'PF-11', 
    'PF-2', 
    'PF-3', 
    'PF-4', 
    'PF-5', 
    'PF-6',
    'PF-7', 
    'PF-8', 
    'PF-9'
]
#'''
#'''
list_attacker = []
with open("set_request.json", "r+") as f:
    readJSONfile = json.load(f)
    for m in readJSONfile:
        att = str(m)
        list_attacker.append(att)
f.close()
list_attacker = sorted(list_attacker)
#'''
for attacker in list_attacker:
    cod = attacker[3:5]
    cod.replace(" ", "")
    check = check_cod_id(cod)
    if check == "false":
        print("profile not found")
    else:
        email = check[0]
        password = check[1]
    with open("set_request.json", "r") as c:
        readJSONfile = json.load(c)
        temp = readJSONfile[attacker]
        i=0
        request = []
        while i < counting:
            request.append(temp[first_element+i])
            i=i+1
        print(request)
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        #necessary for take out the chrome notifications
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        #chrome_options.add_argument("user-data-dir=selenium")
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
        driver.maximize_window()
        delete_cache()
        driver.get('https://www.facebook.com')
        print("..........................................................")
        print("attacker: "+attacker)
        #chrome://settings/
        time.sleep(2)
        #close cookies
        closed_everything = True
        while closed_everything:
            try:
                driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy']").click()
            except NoSuchElementException:
                print("no cookie")
                closed_everything = False
            time.sleep(3)

        time.sleep(2)

        insert_email = driver.find_element_by_id('email')
        insert_email.send_keys(email)
        insert_pwd = driver.find_element_by_id('pass')
        insert_pwd.send_keys(password)
        time.sleep(2)

        #click button to login
        try:
            try:
                driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()
            except:
                driver.find_element_by_xpath("//button[@id='loginbutton']").click()

            time.sleep(5)
            count = 0
            for a in request:
                print("-------------------------------- profile:")
                with open("../victims.json", "r") as f:
                    readJSONfile = json.load(f)
                    victim = request[count][0:3]
                    index = request[count][4:-1]
                    temp = readJSONfile[victim]
                    url = temp[int(index)]
                    print(url)
                    add(attacker, url, victim)
                f.close()
                count=count+1
                #add(cod_id, email, password, first_element, counting)

        except:
            print("No clicked")
            print(Exception)
    #driver.quit()
