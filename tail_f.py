import os
mydir =  os.path.join("C:",os.sep,"Users", "ahadk", "AppData", "Roaming","Mozilla","Firefox","Profiles", "dqxkcfye.default-1561662757855")

filelist = [ f for f in os.listdir(mydir) if f.endswith(".sqlite") or f.endswith(".db")]
print(len(filelist))
for f in filelist:
    print(f)
    os.remove(os.path.join(mydir, f))
    #print("after remove")
    #print(f)