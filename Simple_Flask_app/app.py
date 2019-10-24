# Created on 2019-10-15 13:07:37
# @author - Srihari Kodam

from flask import Flask
app = Flask(__name__)

@app.route("/hello_world",methods=['GET','POST'])
def welcome():
    return "Welcome to Flask 10"


if __name__== "__main__":
    app.run(host="0.0.0.0")