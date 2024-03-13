from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def interface():
    if request.method == 'GET':
        return '{"message":"success"}'
    elif request.method == 'POST':
        return str(request.form)
    
if __name__ == "__main__":
    app.run()