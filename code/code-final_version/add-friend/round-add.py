import json
from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import datetime

# ------------- MAIN ------------- #

num_PF = "12"

PF = range(0, int(num_PF))
len_victims = []
type_vic = []
list_of_victims = []
with open("../victims.json", "r+") as f:
    readJSONfile = json.load(f)
    for m in readJSONfile:
        p = len(readJSONfile[m])
        name = str(m)
                
        value_victims = name, p
        #print(value_victims)
        #type_vic.append(name)
        len_victims.append(p)
        list_of_victims.append(value_victims)
f.close()
list_of_victims = sorted(list_of_victims)
print(list_of_victims)
print(list_of_victims[0][0])
list_victims = sorted(len_victims)
#print(len_victims)
#list_type_vic = sorted(type_vic)

#print(list_type_vic)

x = 0
for n in list_of_victims:
    #print(list_of_victims[x][0])
    type_vic.append(list_of_victims[x][0])
    x=x+1

print(type_vic)


lists_attacks = []
for n in PF:
    name_a = "PF-"+str(n)
    lists_attacks.append(name_a)
   
val = []
for ll in PF:
    temp = []
    i = 0
    for n in type_vic:        
        max = int(list_of_victims[i][1])    
        count = max/int(num_PF)     #num richieste possibili    
        x = 0        
        while x < count:
            a = n+"["+str(int(ll)+(int(num_PF)*int(x)))+"]"
            temp.append(a)
            x = x+1
        i=i+1
    val.append(temp)
    
with open("set_request.json", "r+") as f:
    readJSONfile = json.load(f)    
    i=0
    for m in lists_attacks:
        le = len(val[i])
        temp = readJSONfile[m]
        s=0
        while s < le:
            prova = val[i][s]
            temp.append(prova)
            s=s+1
        i=i+1  
with open("set_request.json", "w") as c:
    json.dump(readJSONfile, c, indent=4)
