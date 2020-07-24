from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "<b>You are on Landing Page!"

@app.route('/<name>/')
def helloName(name) :
    return 'Hello {} '.format(name)




if __name__ == '__main__':
    app.run()