import json

PF = [
    "PF-0", "PF-1", "PF-2", "PF-3", "PF-4", "PF-5", "PF-6", "PF-7", "PF-8",
    "PF-9", "PF-10", "PF-11"
]
vic = [
    "FT2", "FT3", "FT4", "FF2", "FF3", "FF4", "MT2", "MT3", "MT4", "MF2",
    "MF3", "MF4"
]

val_attacker = [
    "MT4", "MF4", "MF2", "MT3", "MF3", "MT2", "FT4", "FF4", "FF2", "FT3",
    "FF3", "FT2"
]

with open("../code-final_version/analizer/distribution/distribution_update.json","r+") as s:
    readJSONfile = json.load(s)
    i = 0
    for r in readJSONfile:
        print("\n>> " + r + " ---------------------------------------------------------------------------------------------------------------")
        count = 0
        best = []
        almost_best = []
        quite_best = []
        not_best = []
        pro = readJSONfile[vic[i]]
        #print(pro)
        c = 0
        for n in PF:
            x = pro.get(n)
            if x == 0:
                #print("\t"+val_attacker[c] + ":\t≈ 1%")
                count = count + 1
                not_best.append(val_attacker[c])
            if x == 1:
                #print("\t"+val_attacker[c] + ":\t≈ 33%")
                count = count + 33
                quite_best.append(val_attacker[c])
            if x == 2:
                #print("\t" + val_attacker[c] + ":\t≈ 66%")
                count = count + 66
                almost_best.append(val_attacker[c])
            if x == 3:
                #print("\t" + val_attacker[c] + ":\t≈ 99%")
                count = count + 99
                best.append(val_attacker[c])
            c = c + 1
        media = count / 12
        print("\tgrado di accettabilita media = " + str(round(media, 2)) + "%")
        print("\n\tProfili che la vittima di tipo " + vic[i] +
              " accetta più facilmente: ")
        if best != []:
            print("\t\tcon probabilità ≈99% =\t" + str(best))
        if almost_best != []:
            print("\t\tcon probabilità ≈66% =\t" + str(almost_best))
        if quite_best != []:
            print("\t\tcon probabilità ≈33% =\t" + str(quite_best))
        if not_best != []:
            print("\t\tcon probabilità ≈1%  =\t" + str(not_best))
        i = i + 1
s.close()
