import json
import datetime

from matplotlib import pyplot as plt

today = datetime.date.today()
attacker = []
with open("../add-friend/request-log.json", "r+") as f:
    readJSONfile_att = json.load(f)
    for m in readJSONfile_att:
        attacker.append(str(m))
f.close()
txt=""
for x in attacker:
    str_first = x+" request to: "
    with open("../add-friend/request-log.json", "r+") as f:
        asse_x=[]
        asse_y=[]
        readJSONfile = json.load(f)
        check = readJSONfile[x]
        num_friend_request = len(check)
        s = 0
        found = []
        while s < num_friend_request:
            type_v = check[s]["type"]
            found.append(type_v)
            s=s+1
        #print(found)
        my_dict = {i: found.count(i) for i in found}
        l = my_dict.items()
        list_something = list(l)
        #print(list_something)
        vict = [("FT2", 0), ("FT3", 0), ("FT4", 0), ("FF2", 0), ("FF3", 0),
                ("FF4", 0), ("MT2", 0), ("MT3", 0), ("MT4", 0), ("MF2", 0),
                ("MF3", 0), ("MF4", 0)]
        acc_x = []
        acc_y = []
        for prova in list_something:
            valx = prova[0] #guardo le richieste fatte
            valy = prova[1] #guardo le richieste fatte
            asse_x.append(valx) #guardo le richieste fatte
            asse_y.append(valy)  #guardo le richieste fatte
            #guardo chi ha accettato le richieste
            ok = open("distribution/distribution_"+str(today)+".json", "r")
            json_object = json.load(ok)
            ok.close()
            #print(json_object[type_vic])
            pp = json_object[valx]
            acc_y.append(pp[x])
            acc_x.append(valx)


        #print(vict)
        '''
        directory = "report_request/"+x+"_report-request.png"
        plt.figure()
        plt.title(str_first)
        plt.bar(asse_x, asse_y, color=(0.1, 0.5, 0.6))
        plt.savefig(directory)
        '''
        plt.figure()
        directory = "report_acceptance/" + x + "_report-acceptance.png"
        plt.title("friend requests accepted from "+x)
        plt.bar(acc_x, acc_y, color=(0.1, 0.5, 0.6))
        plt.savefig(directory)
   

        v=0



        #found = list(dict.fromkeys(found))
        #print(found)
        #txt = txt + str_first + "\n" + str(my_dict) + "\n"
'''
file_name = "report-request.txt"
file = open(file_name, "w+")
file.write(txt)
file.close()'''