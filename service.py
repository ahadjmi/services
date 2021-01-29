from flask import Flask,request,Response,stream_with_context
import endpoints as points
from pathlib import Path
from datetime import datetime
from time import sleep

app = Flask(__name__)

@app.route('/start/',methods=['GET'])
def start_browser():
   name = request.args.get("name")
   url = request.args.get("url")
   points.start_fun(name,url)
   return str(name) + " browser has been started"


@app.route('/stop/',methods=['GET'])
def stop_browser():
   name = request.args.get("name")
   points.stop_fun(name)
   return str(name) + " browser has been closed"


@app.route('/clear/',methods=['GET'])
def clear_history():
   browser = request.args.get("browser")
   history=points.clear_fun(browser)
   return "All history cleared : " + str(history)

@app.route('/show/',methods=['GET'])

def show_history():
   browser = request.args.get("browser")
   history=points.show_url(browser)
   return "All history cleared : " + str(history)

@app.route('/latesturl/',methods=['GET'])
def latest_url():
   browser = request.args.get("browser")
   row = points.latest_url_fun(browser)
   return "Latest url history is : "+ str(row)
   
@app.route("/time/")
def time():
   def streamer():
      while True:
         yield "<p>{}</p>".format(datetime.now())
         sleep(1)
   return Response(streamer())



@app.route('/',methods=['GET'])
def test():
   return "Welcome to Browser. features are, start,stop,clear,latesturl"

@app.route('/log/')
def tailf():
   
   def watch(fn,count):
      count = count-10
      fp = open(fn, 'r')
      while True:
         new = fp.readline()
         if new and count==0:
            yield "<p>{}</p>".format(new)
                       
         elif count>0:
            count = count-1
         else:
            sleep(0.5)
            continue

   fn = Path('C:/Users/ahadk/webservice/example.txt') #your location of file
   #fn = 'example.txt'
   fp = open(fn, 'r')
   count=0

   for line in fp:
      count += 1
   fp.close()
   # for hit_sentence in watch(fn,count):stream_with_context(generate())
   return Response(watch(fn,count), 'text')

if __name__ == '__main__':
   app.run(debug=True)
