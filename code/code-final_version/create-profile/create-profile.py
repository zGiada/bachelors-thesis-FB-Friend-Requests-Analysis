import json
import random
from random import randint
import sys
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

today = datetime.date.today()

if len(sys.argv) != 6:  #nome_script, cod_id, gender, realimg, age, agehide
    print("incorrect number of parameters entered")
    sys.exit()

nome_script, cod_id, gender, realimg, age, agehide = sys.argv

if gender == "female":
    label = "F"
if gender == "male":
    label = "M"

#name
with open("../dataset/dataset-name.json", "r") as f:
    readJSONfile = json.load(f)
    temp = readJSONfile[gender]
    value = randint(1, len(temp)-1)
    i=1
    for entry in temp:
        if (value == i):
            name = entry["name"]
        i=i+1
f.close()

#surname
with open("../dataset/dataset-surname.json", "r") as f:
    readJSONfile = json.load(f)
    temp = readJSONfile["surnames"]
    value = randint(1, len(temp)-1)
    i = 1
    for entry in temp:
        if (value == i):
            surname = entry["surname"]
        i = i + 1
f.close()

#real_img
if (realimg == "true"):
    real_img = True
    label = label+"T"
else:
    real_img = False
    label = label+"F"

#working with age
birthday_year = today.year - int(age)
birthday_month = randint(1, (today.month) - 1)
birthday_day = randint(1, 28)

if (int(age)>18 and int(age)<50):
    age_range = 2
    label = label+"2"
else: 
    if (int(age) >= 50):
        age_range = 3
        label = label+"3"
    else:
        age_range = 4
        label = label+"4"
        
if (agehide == "true"):
    age_hide = True    
else:
    age_hide = False


#password
minuscole = ('abcdefghijklmnopqrstuvwxyz')
maiuscole = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
caratterispeciali = ('!$-_#=?')
password = random.choice(maiuscole)
for i in range(0, 4):
    password += random.choice(minuscole)
password += str(randint(0, 9))
password += random.choice(caratterispeciali)

#hometown
with open("../dataset/dataset-city.json", "r") as f:
    readJSONfile = json.load(f)
    temp = readJSONfile["hometown"]
    value = randint(1, len(temp)-1)
    i = 1
    for entry in temp:
        if (value == i):
            city = entry["city"]
        i = i + 1
f.close()

#occupation
with open("../dataset/dataset-occupation.json", "r") as f:
    readJSONfile = json.load(f)
    temp = readJSONfile[gender]
    value = randint(1, len(temp)-1)
    i = 1
    for entry in temp:
        if (value == i):
            occupation = entry["occupation"]
        i = i + 1
f.close()
if (int(age) >= 65 and gender == "female"):
    occupation = "Pensionata"
if (int(age) >= 65 and gender == "male"):
    occupation = "Pensionato"
'''
#email
PATH = "/home/giada/Scrivania/chromedriver"
#necessary for take out the chrome notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.maximize_window()
driver.get('https://emailfake.com/')
time.sleep(3)
email = ((name + "." + surname + "." + age).lower()).replace(" ", "")
driver.find_element_by_id('userName').clear()
time.sleep(3)
driver.find_element_by_id('userName').send_keys(email)
time.sleep(3)
driver.find_element_by_id('copbtn').click()
time.sleep(3)
email = driver.find_element_by_xpath("//*[@id='email_ch_text']").text
time.sleep(3)
driver.close()
'''
email = ""
#create profile
try:
    item_data = {}
    with open("../dataset/profili-fake.json", "r+") as f:
        readJSONfile = json.load(f)
        temp = readJSONfile[gender]
        item_data["label"] = label
        item_data["cod_id"] = int(cod_id)
        item_data["name"] = name
        item_data["surname"] = surname
        item_data["email"] = email
        item_data["pwd"] = password
        item_data["real_img"] = bool(real_img)
        item_data["age_range"] = age_range
        item_data["age_hide"] = bool(age_hide)
        item_data["d"] = birthday_day
        item_data["m"] = birthday_month
        item_data["y"] = birthday_year
        item_data["hometown"] = city
        item_data["real_occupation"] = occupation
        temp.append(item_data)

    with open("../dataset/profili-fake.json", "w") as c:
        json.dump(readJSONfile, c, indent=4)
    print("profile created")
except:
    print("profile not created")
