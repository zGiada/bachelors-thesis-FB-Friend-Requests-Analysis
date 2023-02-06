import json

y = [
    "PF-0", "PF-1", "PF-2", "PF-3", "PF-4", "PF-5", "PF-6", "PF-7", "PF-8",
    "PF-9", "PF-10", "PF-11"
]
vic = [
    "FT2", "FT3", "FT4", "FF2", "FF3", "FF4", "MT2", "MT3", "MT4", "MF2",
    "MF3", "MF4"
]

for n in vic:
    print(n)
    modify = open("save_distribution.json", "r")
    json_object = json.load(modify)
    modify.close()
    pp = json_object[n]
    for l in y:
        pp[l] = 0
    modify = open("save_distribution.json", "w")
    json.dump(json_object, modify, indent=4)
    modify.close()