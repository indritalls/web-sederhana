from flask import Flask
import flask

app = Flask(__name__)

@app.route('/indri')
def indri():
    return "<h1>hello<h1>"

if __name__=="__main__":
    app.run (debug=True)
