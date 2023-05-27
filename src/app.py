from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Python Flask'
 
if __name__ == "__main__":
    app.debug = True
    app.run()
