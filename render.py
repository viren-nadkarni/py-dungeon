from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config.update(
    SECRET_KEY = 'AMN',
    DEBUG = True
)

@app.route('/')
def hello(name=None):
    user = { 'name' : 'hello'}
    return render_template('index.html',n=user)

if __name__ == "__main__":
	app.run()	

