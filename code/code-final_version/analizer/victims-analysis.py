import os
import json
import matplotlib.pyplot as plt
import locale;  
os.environ["PYTHONIOENCODING"] = "utf-8"; 
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8"); 

item_data = {}

#print("class = "+classifier)
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
        #print(p)
f.close()
elements = sorted(item,key=lambda x: x[1], reverse=True)
print("Tot = "+str(count))
print('\n'.join(map(str, elements)))

plt.bar(x, y, color=(0.1, 0.5, 0.6))
plt.title("victims' distribution")
plt.show()
name = "victims_distribution.png"
plt.show()
