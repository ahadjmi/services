import webbrowser
import os
import sqlite3
import platform
from pathlib import Path
import shutil
user_os = platform.system()

def start_fun(name,url):
    global b_path
    if name == 'chrome' and user_os == 'Windows':
        b_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    elif name == 'firefox' and user_os == 'Windows':
        b_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'

    elif name == 'chrome' and user_os == 'Linux':
        b_path = '/usr/bin/google-chrome %s'

    elif name == 'firefox' and user_os == 'Linux':
        b_path = '/usr/bin/firefox %s'

    elif name == 'chrome' and user_os == 'Darwin' or user_os == 'Java':
        b_path = 'open -a /Applications/Google\ Chrome.app %s'

    webbrowser.get(b_path).open(url)


def stop_fun(name):

    if name=='chrome':
        os.system("taskkill /im chrome.exe /f")
    else:
        os.system("taskkill /im firefox.exe /f")


def clear_fun(browser):
    history = 'Cleared all history, caches, downloads, password successfully'
    if browser == 'chrome':
        mydir = Path('C:/Users/ahadk/AppData/Local/Google/Chrome/User Data/Default')
        filelist = [f for f in os.listdir(mydir) if f.endswith(".sqlite") or f.endswith(".db")]
        print(len(filelist))
        for f in filelist:
            print(f)
        # c = conn.cursor()
        # #result = True
        # #id = 0
        # history = []
        # # while result:
        # #     result = False
        # ids = []
        # for row in c.execute('SELECT url FROM urls WHERE MAX(id)'):
        #     #print(row)
        #     id = row[0]
        #     ur = row[1]
        #     ids.append((id,))
        #     history.append((ur,))
        #
        # #c.executemany('DELETE FROM urls WHERE id=?', ids)
        # conn.commit()
        # conn.close()
        return history

    else:
        mydir = os.path.join("C:",os.sep,"Users", "ahadk", "AppData", "Roaming","Mozilla","Firefox","Profiles", "dqxkcfye.default-1561662757855")
        filelist = [f for f in os.listdir(mydir) if f.endswith(".sqlite") or f.endswith(".db")]
        print(len(filelist))
        for f in filelist:
            print(f)
            os.remove(os.path.join(mydir, f))
        return history

def show_url(browser):
    if browser == 'chrome':
        conn = sqlite3.connect('C:/Users/ahadk/AppData/Local/Google/Chrome/User Data/Default/History')
        c = conn.cursor()
        # result = True
        # id = 0
        history = []
        # while result:
        #     result = False
        ids = []
        for row in c.execute('SELECT id, url FROM urls'):
            # print(row)
            id = row[0]
            ur = row[1]
            ids.append((id,))
            history.append((ur,))

        #c.executemany('DELETE FROM urls WHERE id=?', ids)
        #conn.commit()
        conn.close()
        return history

    else:
        path = os.path.join("C:", os.sep, "Users", "ahadk", "AppData", "Roaming", "Mozilla", "Firefox", "Profiles",
                            "dqxkcfye.default-1561662757855", "places.sqlite")
        conn = sqlite3.connect(path)
        c = conn.cursor()
        result = True
        id = 0
        history = []
        # while result:
        # result = False
        ids = []
        for row in c.execute('SELECT id, url FROM moz_places'):
            # print(row)
            id = row[0]
            ur = row[1]
            ids.append((id,))
            history.append((id, ur,))

        # c.executemany('DELETE FROM moz_places WHERE id=?', ids)
        # conn.commit()
        conn.close()
        return history

def latest_url_fun(browser):
    global latest
    source = 'C:/Users/ahadk/AppData/Local/Google/Chrome/User Data/Default/History'
    destination = 'C:/Users/ahadk/Desktop/webservice/tempfile'
    shutil.copy2(source,destination)
    print('coppedd')
    if browser=='chrome':
        #conn = sqlite3.connect('C:/Users/ahadk/AppData/Local/Google/Chrome/User Data/Default/History')
        conn = sqlite3.connect(str(destination) +'/History')
        c = conn.cursor()

        result = True
        id = 0
        while result:
            result = False
            max_id=0
            for row in c.execute('SELECT id, url FROM urls'):
                id = row[0]
                ur = row[1]
                if max_id < id:
                    max_id = id
                    latest = ur
        #print(row)
        conn.close()
        return latest
    else:
        path = os.path.join("C:", os.sep, "Users", "ahadk", "AppData", "Roaming", "Mozilla", "Firefox", "Profiles",
                            "dqxkcfye.default-1561662757855", "places.sqlite")
        conn = sqlite3.connect(path)
        c = conn.cursor()
        result = True
        id = 0
        max_id = 0
        for row in c.execute('SELECT id, url FROM moz_places'):
            id = row[0]
            ur = row[1]
            if max_id < id:
                max_id = id
                latest = ur

        conn.close()
        return latest


