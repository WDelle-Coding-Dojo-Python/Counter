from typing import Counter
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Why hello there'

@app.route('/')
def index():
    if 'mycounter' in session:
        print('yes')
        session['mycounter']= session['mycounter']+1
    else:
        print("bad")
        session['mycounter'] = 0
    return render_template("index.html")

@app.route('/destroy_session')
def kill_page():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)