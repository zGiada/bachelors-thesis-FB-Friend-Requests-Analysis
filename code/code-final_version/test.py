import json
import sys


if len(sys.argv) != 2:
    print("incorrect number of parameters entered")
    sys.exit()

nome_script, round = sys.argv

tit = [ 1, 1, 2, 3, 3, 2, 3, 3, 3, 3,
        2, 4, 2, 2, 1, 3, 3, 3, 2, 3,
        2, 2, 2, 3, 2, 3, 1, 5, 2, 3, 3, 3, 1,
        4, 1, 3, 2, 3, 1, 2, 3, 1, 3, 1, 3, 1]
counting = tit[int(round)]
first_element = 0
r=0
while r < int(round):
    first_element = first_element + tit[r]
    r=r+1

type_vic = []
with open("victims.json", "r+") as f:
    readJSONfile = json.load(f)
    for m in readJSONfile:
        name = str(m)
        type_vic.append(name)
f.close()
list_type_vic = sorted(type_vic)
#print(list_type_vic)

list_attacker = []
#attacker = "PF-"+str(cod_id)
with open("C:/Users/giada/Desktop/Stage/Report-Stage/code-final_version/add-friend/set_request.json", "r+") as f:
    readJSONfile = json.load(f)
    for m in readJSONfile:
        att = str(m)
        list_attacker.append(att)
f.close()
list_attacker = sorted(list_attacker)

for attacker in list_attacker:
    with open("C:/Users/giada/Desktop/Stage/Report-Stage/code-final_version/add-friend/set_request.json", "r") as c:
        readJSONfile = json.load(c)
        temp = readJSONfile[attacker]
        print("attacker = "+attacker)
        i=0
        request = []
        while i < counting:
            request.append(temp[first_element+i])
            i=i+1
        print(request)
