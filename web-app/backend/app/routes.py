from app import app, socket, db
from flask import request
from app.collection.collection import Collection_Thread, start_collection, stop_collection
from app.models import History

thread = Collection_Thread()

@app.route('/', methods=['GET'])
def index():
    return 'test message'

@app.route('/collection/POST/start', methods=['GET', 'POST'])
def collect_data():
    global thread
    print(thread.collecting)
    if thread.collecting is False:
        hist = History()
        start_collection(thread, hist)
        return 'Sending task to start collection'
    else:
         return 'Collection already running'

@app.route('/collection/POST/stop', methods=['GET', 'POST'])
def stop_collecting_data():
    global thread
    if thread.collecting is True:
        stop_collection(thread)
        return 'Sending task to stop collection'
    return 'No collection currently running'


#TODO: After the microproccesor class is implemented interface this API with that class
@app.route('/microprocessor/POST/values', methods=['GET', 'POST'])
def modify_microprocessor():
    micro_state = request.json
    return 'Sent information to MicroProcessor'
