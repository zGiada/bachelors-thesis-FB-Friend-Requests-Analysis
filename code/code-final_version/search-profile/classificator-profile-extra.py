from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import re
import os
import json
import locale;  
os.environ["PYTHONIOENCODING"] = "utf-8"; 
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8"); 
#print(myText.encode('utf-8', errors='ignore'))

PATH = "/home/giada/Scrivania/chromedriver"
#necessary for take out the chrome notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
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
                #with open('profile.png', 'wb') as file:
                #    l = driver.find_element_by_xpath('//*[@alt="'+img_alt+'"]')
                #    file.write(l.screenshot_as_png)
                if "person" in img_alt:
                    return "T"
                else:
                    return "F"
            except NoSuchElementException:
                return "F"
        except NoSuchElementException:
            '''
            Con YOLO controllare //*[@id="mount_0_0_QZ"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/svg/g/image
            (immagine del profilo presente ma non cliccabile)
            Prova con link: https://www.facebook.com/matteo.zerbinato.1
            '''
            return "F"

def ageProfile():
    time.sleep(2)
    try:
        #save the div's text content where there's the born's year
        capture = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
        time.sleep(2)
        #save data in a temp file
        with open('copy2.txt', 'w') as wf:
            txt = (capture +"\n\n--------------------------")
            wf.write(txt.encode('utf-8', errors='ignore'))
            wf.close()
        #regular expression to find 4 numbers 
        regexp = re.compile(r"\d{4}")
        find = False
        file = open('copy2.txt', 'r')
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
        file = open('copy2.txt', 'r')
        for line in file.readlines():
            if "Uomo" in line:
                gender = "M"
                find = True
            if "Donna" in line:
                gender = "F"
                find = True
        file.close()
        
        if find:
            os.remove("copy2.txt")
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
        with open("../dataset/dataset-name.json", "r") as f:
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
        os.remove("copy2.txt")
        return g
    except:
        pass

def classificator(url,gender,real_img,age):
    item_data = {}
    
    classifier = gender+real_img+age
    print("class = "+classifier)
    print("Ok? ")
    try: 
        x = raw_input()
    except Exception as err:
        print(err)
    if x == "OK":
        pass
    else:
        classifier = x
    print("new classifier = "+classifier)
    
    with open("../victims.json", "r+") as f:
        readJSONfile = json.load(f)
        temp = readJSONfile[classifier]
        x = 0
        stop = False
        if len(temp) < 500:
            alreadyExist = False
            while x < len(temp):
                ind = temp[x]
                if ind in url:
                    alreadyExist = True                
                x += 1
        else:
            stop = True
            
    f.close()
    if stop:
        print("max range already catch")
        with open('out.txt', 'a') as wf:                           
            txt = classifier+","+url            
            wf.write(txt)
            wf.close()   
    else:
        if alreadyExist:
            print("profile already exists")
        else:
            with open("extra-profile.json", "r+") as f:
                readJSONfile = json.load(f)
                temp = readJSONfile[classifier]                
                temp.append(url)
            with open("extra-profile.json", "w") as c:
                json.dump(readJSONfile, c, indent=4)
            print("save victim")

# ------------------------------------------------------------------------ MAIN ------------------------------------------------------------------------
if len(sys.argv) != 3:  #nome_script, cod_id
    print("incorrect number of parameters entered")
    sys.exit()
    
nome_script, cod_id, filetxt = sys.argv

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
        time.sleep(2)
        file = open(filetxt, 'r')
        for line in file.readlines():
            driver.get(line)        
            try:
                ele = driver.find_element_by_xpath("//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l cbu4d94t taijpn5t k4urcfbm']")
                p = ele.get_attribute("aria-label")  
                if p == "Segui":
                    add = False
                if p == "Messaggio":
                    add = False
                if p == "Messaggi":
                    add = False
                if p == "Vedi i messaggi":
                    add = False
                if p == "Aggiungi":
                    add = True
            except:
                add = False
            
            if add:            
                real_img = imgProfile()
                print("real_img: " + real_img)

                if "profile.php" in line:
                    link_age_gender = line + "&sk=about_contact_and_basic_info"
                    link_city = line + "&sk=about"
                    link_occupation = line + "&sk=about_work_and_education"
                else:
                    link_age_gender = line + "/about_contact_and_basic_info"
                    link_city = line + "/about"
                    link_occupation = line + "/about_work_and_education"

                # AGE check
                driver.get(link_age_gender)
                time.sleep(2)
                age = ageProfile()
                #print("age_range: " + age)
                gender = genderProfile()
                #print("gender: "+gender)
                '''
                # HOMETOWN check
                driver.get(link_city)
                time.sleep(2)
                city = selectCity() #return T if is hide, else F 
                if city == "T":
                    hometown = "T"
                    save_home = "null"
                else:
                    hometown = "F"
                    save_home = city
                #print("save_home: " + save_home)
                #print("hometown_hide: " + hometown)

                # OCCUPATION check
                driver.get(link_occupation)
                time.sleep(2)
                occupation_value = selectOccupation()
                #print("occupation_value: " + occupation_value)
                '''
                #line = url
                #print("line: "+line)
                classificator(line,gender,real_img,age)
            else:
                print("impossible to add this profile")
        file.close()
        driver.close()


    except:
        print("No clicked")
