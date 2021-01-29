from flask import Flask, render_template
from flask_socketio import SocketIO, send,emit
from pathlib import Path
from datetime import datetime
from time import sleep
from threading import Thread, Event
#from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app)
#CORS(app)
thread = Thread()
thread_stop_event = Event()
#file_count = 0
# count = count-10
# while count > 0:
#     count = count-1
#     fp.readline()

@app.route('/')
def index():
    # test_message()
    return render_template('index.html')

def watch(fp,count):
    # global count
    # global fn
    #count = count-10
    #fp = open(fn, 'r')
    while not thread_stop_event.isSet():
        
        new = fp.readline()
        if new and new!='\n' and count==0:
            #print(new)
            socketio.emit('my response', {'data': new })
            #socketio.sleep(5)
        # elif count>0:
        #     count = count-1
           
        else:
            socketio.sleep(1)
            #continue
        
        

@socketio.on('connect')
def test_connect():
    global thread
    print('Client connected')
    fn = Path('C:/Users/ahadk/Desktop/webservice/example.txt') #your location of file
    #fn = 'example.txt'
    fp = open(fn, 'r')
    count=0
    for line in fp:
        count += 1
    fp.close
    fp = open(fn, 'r')
    while count>0:
        new = fp.readline()
        if count<=10 and count>0:
            emit('my response', {'data': new })
            count = count-1
        else:
            count = count-1
    #fp.close
    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        #emit('my response', {'data': "Connected" })
        print("Starting Thread")
        thread = socketio.start_background_task(watch,fp,count)
    # fn = Path('C:/Users/ahadk/webservice/example.txt') #your location of file
    # #fn = 'example.txt'
    # fp = open(fn, 'r')
    # count=0

    # for line in fp:
    #    count += 1
    # fp.close()
    # #msg = ['ashif','adil','ahad','ahmad']
    # watch(fn,count)
    #emit('my response', {'data': 'Connected' })

      
# @socketio.on('my event')
# def test_message1(message):
#     emit('my response', {'data': message['data']})



# @socketio.on('logs')
# def test_message():
#     fn = Path('C:/Users/ahadk/webservice/example.txt') #your location of file
#     #fn = 'example.txt'
#     fp = open(fn, 'r')
#     count=0

#     for line in fp:
#        count += 1
#     fp.close()
#     socketio.emit('my response', {'data': count })


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected') 

# @socketio.on('message')
# def handleMessage(msg):
#     print("Message: " + msg)
#     send(msg, broadcast=True)
    #return "<p>{}</p>".format(msg)

# @app.route('/',methods=['GET'])
# def tailf():
#     handleMessage('Hello Abdul Ahad Khan')
#     handleMessage('Hello guest')

# @app.route('/log',methods=['GET'])
# def tailf():
   
#    def watch(fn,count):
#       count = count-10
#       fp = open(fn, 'r')
#       while True:
#          new = fp.readline()
#          if new and count==0:
#             yield "<p>{}</p>".format(new)
                       
#          elif count>0:
#             count = count-1
#          else:
#             sleep(0.5)
#             continue

#    fn = Path('C:/Users/ahadk/webservice/example.txt') #your location of file
#    #fn = 'example.txt'
#    fp = open(fn, 'r')
#    count=0

#    for line in fp:
#       count += 1
#    fp.close()
#    for hit_sentence in watch(fn,count):#stream_with_context(generate())
#         print(hit_sentence)


if __name__ == '__main__':
    socketio.run(app,debug=True)