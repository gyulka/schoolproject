import os
from flask import Flask, request, render_template, session, redirect, Blueprint, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)


@app.route('/')
def base():
    print(request.args)
    return render_template('index.html',imgs=['pic1.jpg','pic2.jpg','pic3.jpg',])



@app.route('/informer')
def iformer():
    return render_template('informer.html')


@app.route('/page1')
def page1():
    return render_template('index.html')


@app.route('/promare')
def page2():
    return render_template('promare.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
