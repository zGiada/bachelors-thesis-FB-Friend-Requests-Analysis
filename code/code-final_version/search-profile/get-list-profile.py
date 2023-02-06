import json
from random import randint
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/giada/Scrivania/chromedriver"
#necessary for take out the chrome notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.maximize_window()


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

def find_name(type_victim):
    if type_victim == "f":
        gender = "female"
    if type_victim == "m":
        gender = "male"
    with open("../dataset/dataset-name.json", "r") as f:
        readJSONfile = json.load(f)
        temp = readJSONfile[gender]
        value = randint(1, len(temp)-1)
        i=1
        for x in temp:
            if (value == i):
                return x["name"]
            i=i+1
    f.close()

# ----------------------------------------------------------------- MAIN ----------------------------------------------------------------- #
if len(sys.argv) != 3:  #nome_script, cod_id, type_victim
    print("incorrect number of parameters entered")
    sys.exit()

nome_script, cod_id, type_victim = sys.argv

#check fake profile exists
check = check_cod_id(cod_id)
if check == "false":
    print("profile not found")
else:
    email = check[0]
    password = check[1]
    #login
    driver.get('https://www.facebook.com')
    time.sleep(2)

    #close cookies
    try:
        driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy']").click()
    except NoSuchElementException:
        print("no cookie")

    time.sleep(2)
    insert_email = driver.find_element_by_id('email')
    insert_email.send_keys(email)
    insert_pwd = driver.find_element_by_id('pass')
    insert_pwd.send_keys(password)
    time.sleep(2)

    #click button to login
    try:
        driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()
        time.sleep(5)
        try:
            choice = False
            while not choice:
                name = find_name(type_victim)
                print("Name: "+name)
                choice = input("Ok? ")
            try:
                time.sleep(5)
                #https://www.facebook.com/search/people/?q=nome
                url_name = ("https://www.facebook.com/search/people/?q="+name).lower()
                driver.get(url_name)
                try:
                    time.sleep(6)
                    driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l cbu4d94t taijpn5t k4urcfbm']").click()
                except:
                    pass
                try:
                    time.sleep(5)
                    i = 1
                    base = ("https://www.facebook.com/" + name).lower()
                    while i>=0:
                        elems = driver.find_elements_by_xpath("//a[@href]")
                        for elem in elems:
                            line = elem.get_attribute("href")
                            if "https://www.facebook.com/profile.php?id" in line:
                                if "%" in line:
                                    pass
                                else:
                                    if i == 0:
                                        with open('list-profiles.txt', 'a') as wf:
                                            txt = (line)
                                            wf.write(txt + '\n')
                                        wf.close()

                            if base in line:
                                if "%" in line:
                                    pass
                                else:
                                    if i == 0:
                                        with open('list-profiles.txt', 'a') as wf:
                                            txt = (line)
                                            wf.write(txt + '\n')
                                        wf.close()
                        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                        time.sleep(5)
                        print(i)
                        i = i-1
                    time.sleep(5)
                    driver.close()
                except:
                    print("lista amici non trovata")
            except:
                print("not press")
        except:
            print("search input field not found")
    except:
        print("No clicked")
