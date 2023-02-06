import datetime
import json
import os
from matplotlib import pyplot as plt

today = datetime.date.today()

PF = ["PF-0", "PF-1", "PF-2", "PF-3", "PF-4", "PF-5", "PF-6", "PF-7", "PF-8","PF-9", "PF-10", "PF-11"]
vic = ["FT2", "FT3", "FT4", "FF2", "FF3", "FF4", "MT2", "MT3", "MT4", "MF2","MF3", "MF4"]
total_count = []

directory = "report-" + str(today)

parent_dir = "C:/Users/giada/Desktop/Stage/Report-Stage/code-final_version/analizer"
path = os.path.join(parent_dir, directory)
print(path)
os.makedirs(path)

with open("save_distribution.json", "r+") as s:
    readJSONfile = json.load(s)
    # creo i grafici
    i = 0
    while i < len(vic):
        cc = 0
        value = []
        for n in PF:
            m = readJSONfile[vic[i]]
            cv = m[n]
            value.append(cv)
            cc = cc+cv
        total_count.append(cc)
        plt.figure()
        plt.bar(PF, value, color=(0.1, 0.5, 0.6))
        plt.title(str(i) + "- " + vic[i] + " victims that accept friend request")
        string_ti = "in date: " + str(today)
        plt.suptitle(string_ti)
        name = str(today) + " - " + str(i) + "-" + vic[i] + ".png"
        save_path = "" + directory + "/" + name
        plt.savefig(save_path)
        i = i + 1
s.close()
plt.figure()
plt.suptitle("")
plt.bar(vic, total_count, color=(0.3, 0.4, 0.7))
plt.title("total count victims that have accepted the friend request")
save_path = "" + directory + "/total_distribution.png"
plt.savefig(save_path)

name_distr = "distribution/" + "distribution_" + str(today) + ".json"
f = open(name_distr, "w+")
json.dump(readJSONfile, f, indent=4)
f.close()

name_distr = "distribution/distribution_update.json"
f = open(name_distr, "w+")
json.dump(readJSONfile, f, indent=4)
f.close()