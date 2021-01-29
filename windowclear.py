import os
import shutil
from pathlib import Path
#mydir =  os.path.join("C:",os.sep,"Users", "ahadk", "AppData", "Roaming","Mozilla","Firefox","Profiles", "dqxkcfye.default-1561662757855")
source = 'C:/Users/ahadk/AppData/Local/Google/Chrome/User Data/Default'
destination = 'C:/Users/ahadk/Desktop/webservice/tempfile'
mydir = Path('C:/Users/ahadk/AppData/Local/Google/Chrome/User Data/Default')
filelist = [ f for f in os.listdir(mydir) if f=='History' or f=='Login Data' or f=='Media History' or f=='Cookies' ]
print(len(filelist))
os.remove(os.path.join(mydir, 'History'))
for f in filelist:
    #shutil.copy2(str(source)+'/'+ str(f),destination)
    print(f)
    #os.remove(os.path.join(mydir, f))