from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key="@@fortess"

@app.route('/')
def index():

    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1

    print(session['visits'])
    return render_template('session.html')
@app.route('/destroy_session')
def destroy():
    # session.clear()  #NOTE: this clears all keys.
    # session.pop('visits')  #NOTE: this clears a specific key, in this case -> 'visits'
    if 'visits' in session:
        session.clear()
    else:
        raise ValueError('no visits')

    return render_template('session.html')

@app.route('/+2')
def add():
    if 'visits' not in session:
        session['visits'] = 2
    else:
        session['visits'] += 2
    return render_template('session.html')

if __name__== '__main__':
    app.run(debug=True)