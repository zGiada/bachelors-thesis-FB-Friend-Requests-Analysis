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
txt = ""
for x in attacker:
    str_first = x + " request to: "
    with open("../add-friend/request-log.json", "r+") as f:
        asse_x = []
        asse_y = []
        readJSONfile = json.load(f)
        check = readJSONfile[x]
        num_friend_request = len(check)
        s = 0
        found = []
        while s < num_friend_request:
            type_v = check[s]["type"]
            found.append(type_v)
            s = s + 1
        my_dict = {i: found.count(i) for i in found}
        l = my_dict.items()
        list_something = list(l)
        acc_x = []
        acc_y = []
        for prova in list_something:
            valx = prova[0]  #guardo le richieste fatte
            valy = prova[1]  #guardo le richieste fatte
            asse_x.append(valx)  #guardo le richieste fatte
            asse_y.append(valy)  #guardo le richieste fatte

        directory = "report_request/" + x + "_friend-requests-sent.png"
        plt.figure()
        plt.title(str_first)
        plt.bar(asse_x, asse_y, color=(0.1, 0.5, 0.6))
        plt.savefig(directory)
        v = 0
