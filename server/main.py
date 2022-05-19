from flask import Flask
import time

#Web request handlers 
web_app = Flask(__name__)

@web_app.route('/generate-room')
def generate_room():
    return str(time.time())


@web_app.route('/connect/<room_key>')
def connect(room_key):
    return "Ok with " + str(room_key) 




web_app.run(debug = True)