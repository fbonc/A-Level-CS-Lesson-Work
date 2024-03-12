from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
app.secret_key = '1234567890'


@app.route('/', methods = ['POST', 'GET'])
def index():
    filename = r'L6 LT1\Mr. Lomax\flaskdiscussionboard\comments.txt'
    with open(filename, 'r') as file:
        text = file.read()

    if request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        comment = request.form.get('comment')

        if comment:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M")
            today = datetime.date.today()
    
            with open(filename, 'a') as file:
                entry = f"[{current_time}, {today}] {session.get('username', 'Anon')}--:::::--{comment}\n"
                file.write(entry)


    with open(filename, 'r') as file:
        text = file.read()

        return render_template('index.html', text=text, username=session.get('username', 'Anon'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)