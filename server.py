from flask import Flask, render_template, request, redirect, session
import random

rand = random.randint(1, 100)
app=Flask(__name__)
app.secret_key = 'KaiMuller'
print(rand)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if int(request.form['input']) == rand:
        answer = "Correct!"
        return render_template('index.html', answer = answer)
    if int(request.form['input']) < rand:
        answer = (f"Sorry, {request.form['input']} is too low!")
        return render_template('index.html', answer = answer)
    if int(request.form['input']) > rand:
        answer = (f"Sorry, {request.form['input']} is too high!")
        return render_template('index.html', answer=answer)








if __name__=="__main__":
    app.run(debug=True)
