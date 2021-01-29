import sqlite3
import os

db_path = 'C:/Users/ahadk/AppData/Local/Google/Chrome/User Data/Default/Login Data'
                             #os.path.join(os.environ["ahadk"], "AppData", "Local",
                            #"Google", "Chrome", "User Data", "default", "Login Data")
db = sqlite3.connect(db_path)
cursor = db.cursor()
# `logins` table has the data we need
cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
n_logins = len(cursor.fetchall())
print(f"Deleting a total of {n_logins} logins...")
#cursor.execute("delete from logins")
#cursor.connection.commit()