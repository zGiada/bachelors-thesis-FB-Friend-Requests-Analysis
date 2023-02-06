import os
import json
from matplotlib import pyplot as plt
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import sys
import datetime
import locale;
os.environ["PYTHONIOENCODING"] = "utf-8";
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8");

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

def check_url(cod_id):
    with open("../dataset/profili-fake.json", "r") as f:
        readJSONfile = json.load(f)
        not_found = True
        temp = readJSONfile["male"]
        for i in temp:
            if (i["cod_id"] == int(cod_id)):
                url = i["url"]
                not_found = False
        if not_found:
            temp = readJSONfile["female"]
            for i in temp:
                if (i["cod_id"] == int(cod_id)):
                    url = i["url"]
                    not_found = False
    if not_found:
        return "false"
    else:
        return url


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

item_data = {}
item = []
count = 0
x=[]
y=[]
with open("../victims.json", "r+") as f:
    readJSONfile = json.load(f)
    for m in readJSONfile:
        #print(x+" = "+str(len(readJSONfile[x])))
        p = str(m), len(readJSONfile[m])
        x.append(m)
        y.append(len(readJSONfile[m]))
        count = count+len(readJSONfile[m])
        item.append(p)
f.close()
elements = sorted(item,key=lambda x: x[1], reverse=True)
#print("Tot = "+str(count))
#print('\n'.join(map(str, elements)))

#SAVE LIST OF FAKE PROFILE
attacker = ['PF-0', 'PF-1', 'PF-2', 'PF-3', 'PF-4', 'PF-5', 'PF-6', 'PF-7', 'PF-8', 'PF-9', 'PF-10', 'PF-11']
#attacker = ['PF-6']
'''
attacker = []
with open("../add-friend/request-log.json", "r+") as f:
    readJSONfile = json.load(f)
    for m in readJSONfile:
        attacker.append(str(m))
f.close()
#'''
for x in attacker:
    cc=0

    cod = x[3:5]
    cod.replace(" ", "")
    check = check_cod_id(cod)
    if check == "false":
        print("profile not found")
        break
    else:
        email = check[0]
        password = check[1]

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
    #CLOSE COOKIES
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
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()
    except:
        driver.find_element_by_xpath("//button[@id='loginbutton']").click()
    time.sleep(2)
    #
    try:
        personal_profile = driver.find_element_by_xpath("//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi']").click()
    except:
        try:
            personal_profile = driver.find_element_by_xpath("//div[@class='gs1a9yip ow4ym5g4 auili1gw rq0escxv j83agx80 cbu4d94t buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 tgvbjcpo hpfvmrgz rz4wbd8a a8nywdso l9j0dhe7 du4w35lb rj1gh0hx pybr56ya f10w8fjw']").click()
        except:
            personal_profile = check_url(cod)
            driver.get(personal_profile)

    time.sleep(3)
    url_attacker = driver.current_url
    #print(url_attacker)

    if "profile.php" in url_attacker:
        url_attacker = url_attacker + "&sk=friends"
    else:
        url_attacker = url_attacker + "/friends"

    driver.get(url_attacker)
    time.sleep(3)
    i = 3
    #div class con amici j83agx80 btwxx1t3 lhclo0ds i1fnvgqd
    e = driver.find_element_by_xpath("//div[@class='j83agx80 btwxx1t3 lhclo0ds i1fnvgqd']").text
    while i>=0:
        elems = driver.find_elements_by_xpath("//a[@href]")
        #print("------------elems------------")
        for elem in elems:
            line = elem.get_attribute("href")
            #print(line)
            with open('list-href.txt', 'a') as wf:
                txt = (line)
                wf.write(txt + '\n')
            wf.close()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        #print(i)
        i = i-1

    #print("------------check------------")
    with open("../add-friend/request-log.json", "r+") as f:
        readJSONfile = json.load(f)
        check = readJSONfile[x]
        #print("check: " + x + " - " + str(len(check)))
        num_friend_request = len(check)
        s = 0
        print("------------------------------ attacker = "+x)
        while s < num_friend_request:
            check_exist = check[s]["victim"]
            #print("check_exist = " + str(check_exist))
            file = open('list-href.txt', 'r')
            trovata = False
            for l in file.readlines():
                #print("l = "+l)
                if check_exist in l:
                    #print(check_exist + " ok")
                    type_vic = str(check[s]["type"])
                    cc = cc+1
                    modify = open("save_distribution.json", "r")
                    json_object = json.load(modify)
                    modify.close()
                    pp = json_object[type_vic]
                    pp[x] = pp[x] + 1
                    modify = open("save_distribution.json", "w")
                    json.dump(json_object, modify, indent=4)
                    modify.close()
                    trovata = True
                    break
                else:
                    pass
            if not trovata:
                check_type = check[s]["type"]
                #print(" ("+check_type+")"+" NOT ACCEPTED FRIEND REQUEST = "+check_exist)
            file.close()
            s = s + 1
    f.close()
    print("acceptance rate: " + str(cc) + "/" + str(num_friend_request))
    os.remove("list-href.txt")
    #driver.close()
