from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import sys
import re
import os
import json
import locale;
os.environ["PYTHONIOENCODING"] = "utf-8";
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8");
#print(myText.encode('utf-8', errors='ignore'))

PATH = "C:\Program Files (x86)\chromedriver.exe"
#necessary for take out the chrome notifications
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.maximize_window()


def check_cod_id(email_attacker, pwd_attacker):
    with open("../code-final_version/dataset/profili-fake.json", "r") as f:
        readJSONfile = json.load(f)
        not_found = True
        temp = readJSONfile["male"]
        for i in temp:
            if ((i["email"] == email_attacker) and (i["pwd"] == pwd_attacker)):
                email = i["email"]
                password = i["pwd"]
                not_found = False
        if not_found:
            temp = readJSONfile["female"]
            for i in temp:
                if ((i["email"] == email_attacker) and (i["pwd"] == pwd_attacker)):
                    email = i["email"]
                    password = i["pwd"]
                    not_found = False
    if not_found:
        return "false"
    else:
        return email, password

def imgProfile():
    time.sleep(2)
    #check if there's a story, 'cause, in that way, the process to find image profile is different
    try:
        #click oh the story
        driver.find_element_by_xpath("//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id']").click()
        time.sleep(2)
        #there's a tooltip: show the story or show image profile
        select_img = driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb'][last()]").get_attribute('href')
        #go to image link
        driver.get(select_img)
        try:
            time.sleep(2)
            #find the alt tag
            img_alt = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('alt')
            if "person" in img_alt:
                return "T"
            else:
                return "F"
        except Exception as error:
            return "F"
    except NoSuchElementException:
        try:
            #click on image profile
            driver.find_element_by_xpath("//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id']").click()
            try:
                time.sleep(2)
                #find alt tag
                img_alt = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('alt')
                if "person" in img_alt:
                    return "T"
                else:
                    return "F"
            except NoSuchElementException:
                return "F"
        except NoSuchElementException:
            return "F"

def ageProfile():
    time.sleep(2)
    try:
        #save the div's text content where there's the born's year
        capture = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
        time.sleep(2)
        #save data in a temp file
        with open('copy.txt', 'w') as wf:
            txt = (capture +"\n\n--------------------------")
            wf.write(txt)
            wf.close()
        #regular expression to find 4 numbers
        regexp = re.compile(r"\d{4}")
        find = False
        file = open('copy.txt', 'r')
        for line in file.readlines():
            if regexp.search(line):
                if len(line) == 5:
                    year = line
                    find = True
        file.close()
        if find:
            eta = 2021-int(year)
            if eta >= 18 and eta < 50:
                return "2"
            if eta >= 50:
                return "3"
        else :
            return "4"
    except Exception as error:
        print(error)
        driver.quit()

def genderProfile():
    time.sleep(2)
    try:
        find = False
        file = open('copy.txt', 'r')
        for line in file.readlines():
            if "Uomo" in line:
                gender = "M"
                find = True
            if "Donna" in line:
                gender = "F"
                find = True
        file.close()

        if find:
            os.remove("copy.txt")
            return gender
        else :
            return findGender()
    except Exception as error:
        print(error)
        driver.quit()

def findGender():
    try:
        capture = driver.find_element_by_xpath("//div[@class='cbu4d94t j83agx80']").text
        stop = False
        name = ""
        for x in capture:
            if (not stop):
                if x == " ":
                    stop = True
                else:
                    name = name+""+x
        with open("../code-final_version/dataset/dataset-name.json", "r") as f:
            readJSONfile = json.load(f)
            temp = readJSONfile["female"]
            find = False
            for x in temp:
                if (x["name"] == name):
                    find = True
                    g = "F"
            if not find:
                temp = readJSONfile["male"]
                for x in temp:
                    if (x["name"] == name):
                        find = True
                        g = "M"
        f.close()
        os.remove("copy.txt")
        return g
    except:
        pass

def classificator(gender,real_img,age):
    classifier = gender+real_img+age
    print("class = "+classifier)
    print("Ok? ")
    try:
        x = input()
    except Exception as err:
        print(err)
    if x == "OK" or x == "ok":
        pass
    else:
        classifier = x
    #print("new classifier = "+classifier)
    return classifier


def delete_cache():
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData'
               )  # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
    actions.perform()
    time.sleep(5)  # wait some time to finish
    driver.close()  # close this tab
    driver.switch_to.window(driver.window_handles[0])
# ------------------------------------------------------------------------ MAIN ------------------------------------------------------------------------

PF = ["PF-0", "PF-1", "PF-2", "PF-3", "PF-4", "PF-5", "PF-6", "PF-7", "PF-8", "PF-9", "PF-10", "PF-11"]
vic = ["FT2", "FT3", "FT4", "FF2", "FF3", "FF4", "MT2", "MT3", "MT4", "MF2","MF3", "MF4"]
val_attacker = ["MT4", "MF4", "MF2", "MT3", "MF3", "MT2", "FT4", "FF4", "FF2", "FT3", "FF3", "FT2"]

if len(sys.argv) != 4:
    print("incorrect number of parameters entered")
    sys.exit()

nome_script, email_attacker, pwd_attacker, url_vittima = sys.argv

check = check_cod_id(email_attacker, pwd_attacker)
if check == "false":
    print("profile not found")
else:
    email = check[0]
    password = check[1]
    delete_cache()
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
        time.sleep(2)
        driver.get(url_vittima)
        real_img = imgProfile()

        if "profile.php" in url_vittima:
            link_age_gender = url_vittima + "&sk=about_contact_and_basic_info"
        else:
            link_age_gender = url_vittima + "/about_contact_and_basic_info"

        # AGE check
        driver.get(link_age_gender)
        time.sleep(2)
        age = ageProfile()
        #print("age_range: " + age)
        gender = genderProfile()
        #print("gender: "+gender)
        vittima = classificator(gender,real_img,age)
        driver.close()
    except:
        print("No clicked")
count = 0
best = []
almost_best = []
quite_best = []
not_best = []
with open("../code-final_version/analizer/distribution/distribution_update.json","r+") as s:
    readJSONfile = json.load(s)
    for r in readJSONfile:
        #print(r)
        if r == vittima:
            i = 0
            while i < len(PF):
                if vic[i] == r:
                    pro = readJSONfile[vic[i]]
                    c = 0
                    for n in PF:
                        x= pro.get(n)
                        if x == 0:
                            #print(val_attacker[c] + ":\t≈ 1%")
                            count = count + 1
                            not_best.append(val_attacker[c])
                        if x == 1:
                            #print(val_attacker[c] + ":\t≈ 33%")
                            count = count + 33
                            quite_best.append(val_attacker[c])
                        if x == 2:
                            #print(val_attacker[c] + ":\t≈ 66%")
                            count = count + 66
                            almost_best.append(val_attacker[c])
                        if x == 3:
                            #print(val_attacker[c] + ":\t≈ 99%")
                            count = count + 99
                            best.append(val_attacker[c])
                        c=c+1
                    break
                i=i+1
    media = count/12
    print("\n\n---------------------\n>> VICTIM'S URL: " + url_vittima)
    print("\n---------------------\n>> Type of victim: " + vittima)
    #print("\n\tgrado di accettabilita media = "+str(round(media,2))+"%")
    print("\n\tProfili che la vittima di tipo "+vittima+" accetta più facilmente: ")
    if best != []:
        print("\t\tcon probabilità ≈99% =\t" + str(best))
    if almost_best != []:
        print("\t\tcon probabilità ≈66% =\t" + str(almost_best))
    if quite_best != []:
        print("\t\tcon probabilità ≈33% =\t" + str(quite_best))
    if not_best != []:
        print("\t\tcon probabilità ≈1%  =\t" + str(not_best))
s.close()