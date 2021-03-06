from flask import Flask, request, json
from settings import *
import messageHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        data_forward = data
        data = data.get('object')
        while(data.get('fwd_messages',"")!=""):
            data = data.get('fwd_messages')
            data=dict(data[0])
        if(data.get('attachments',"")!=""):
            return 'ok'
        messageHandler.create_answer(data_forward['object'], token)
    return 'ok'